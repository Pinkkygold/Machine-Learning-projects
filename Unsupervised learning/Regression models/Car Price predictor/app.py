from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os
import socket

app = Flask(__name__)

def find_available_port(start_port=5000, max_port=5010):
    """Find an available port starting from start_port"""
    for port in range(start_port, max_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    raise Exception(f"No available ports between {start_port} and {max_port}")

# Global variables to store data and model
df = None
model = None
feature_columns = None

def load_and_preprocess_data():
    """Load and preprocess the car data"""
    global df, feature_columns
    try:
        # Load the dataset
        df = pd.read_csv('CarPrice_Assignment.csv')
        
        # Data preprocessing
        df['Brand'] = df['CarName'].str.split(' ').str.get(0).str.lower()
        df['Brand'] = df['Brand'].replace(['maxda'], 'mazda')
        df['Brand'] = df['Brand'].replace(['toyouta'], 'toyota')
        df['Brand'] = df['Brand'].replace(['vokswagen', 'vw'], 'volkswagen')
        df['Brand'] = df['Brand'].replace(['porcshce'], 'porsche')
        
        # Create a copy for analysis
        df1 = df.copy()
        df1.drop(['car_ID', 'symboling', 'CarName'], axis=1, inplace=True)
        
        # Calculate average price by brand
        avg_price = df1[['Brand', 'price']].groupby('Brand', as_index=False).mean().rename(columns={'price':'brand_avg_price'})
        df1 = df1.merge(avg_price, on='Brand')
        
        # Create brand categories
        df1['Brand category'] = df1['brand_avg_price'].apply(lambda x: 'Budget' if x < 10000
                                                         else ("Mid Range" if 10000 <= x <= 20000
                                                               else "Luxury"))
        return df1
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def train_model():
    """Train the car price prediction model"""
    global df, model, feature_columns
    if df is not None:
        try:
            # Prepare features and target
            x = df.drop('price', axis=1)
            x_encoded = pd.get_dummies(x, drop_first=True) 
            y = df['price']
            
            # Store feature columns for later use
            feature_columns = x_encoded.columns.tolist()
            
            # Split data
            x_train, x_test, y_train, y_test = train_test_split(x_encoded, y, test_size=0.2, random_state=42)
            
            # Train model
            model = LinearRegression() 
            model.fit(x_train, y_train)
            
            # Save model and feature columns
            joblib.dump(model, 'Car_price_model.pkl')
            joblib.dump(feature_columns, 'feature_columns.pkl')
            
            # Calculate model performance
            y_pred = model.predict(x_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            print(f"Model trained successfully!")
            print(f"R² Score: {r2:.4f}")
            print(f"MSE: {mse:.2f}")
            
            return True
        except Exception as e:
            print(f"Error training model: {e}")
            return False
    return False

def get_available_options():
    """Get available options for categorical features"""
    if df is None:
        return {}
    
    categorical_options = {
        'fueltype': sorted(df['fueltype'].unique()),
        'aspiration': sorted(df['aspiration'].unique()),
        'doornumber': sorted(df['doornumber'].unique()),
        'carbody': sorted(df['carbody'].unique()),
        'drivewheel': sorted(df['drivewheel'].unique()),
        'enginelocation': sorted(df['enginelocation'].unique()),
        'enginetype': sorted(df['enginetype'].unique()),
        'cylindernumber': sorted(df['cylindernumber'].unique()),
        'fuelsystem': sorted(df['fuelsystem'].unique()),
        'Brand': sorted(df['Brand'].unique()),
        'Brand_category': sorted(df['Brand category'].unique())
    }
    
    return categorical_options

def prepare_input_features(user_input):
    """Prepare user input for prediction"""
    global feature_columns
    
    # Create a DataFrame with all feature columns initialized to 0
    input_df = pd.DataFrame(0, index=[0], columns=feature_columns)
    
    # Map user input to feature columns
    try:
        # Numerical features
        numerical_features = [
            'wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight',
            'enginesize', 'boreratio', 'stroke', 'compressionratio', 
            'horsepower', 'peakrpm', 'citympg', 'highwaympg', 'brand_avg_price'
        ]
        
        for feature in numerical_features:
            if feature in user_input and feature in input_df.columns:
                input_df[feature] = float(user_input[feature])
        
        # Categorical features (one-hot encoding)
        categorical_mappings = {
            'fueltype': f"fueltype_{user_input.get('fueltype', 'gas')}",
            'aspiration': f"aspiration_{user_input.get('aspiration', 'std')}",
            'doornumber': f"doornumber_{user_input.get('doornumber', 'four')}",
            'carbody': f"carbody_{user_input.get('carbody', 'sedan')}",
            'drivewheel': f"drivewheel_{user_input.get('drivewheel', 'fwd')}",
            'enginelocation': f"enginelocation_{user_input.get('enginelocation', 'front')}",
            'enginetype': f"enginetype_{user_input.get('enginetype', 'ohc')}",
            'cylindernumber': f"cylindernumber_{user_input.get('cylindernumber', 'four')}",
            'fuelsystem': f"fuelsystem_{user_input.get('fuelsystem', 'mpfi')}",
            'Brand': f"Brand_{user_input.get('Brand', 'toyota')}",
            'Brand category': f"Brand category_{user_input.get('Brand_category', 'Mid Range')}"
        }
        
        for feature, encoded_feature in categorical_mappings.items():
            if encoded_feature in input_df.columns:
                input_df[encoded_feature] = 1
        
        return input_df
        
    except Exception as e:
        print(f"Error preparing input features: {e}")
        return None

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Car price prediction page"""
    global df, model, feature_columns
    
    if df is None:
        df = load_and_preprocess_data()
    
    # Get available options for dropdowns
    options = get_available_options()
    
    prediction = None
    error = None
    
    if request.method == 'POST':
        try:
            # Get form data
            user_input = {
                # Numerical features
                'wheelbase': request.form.get('wheelbase', 100.0),
                'carlength': request.form.get('carlength', 175.0),
                'carwidth': request.form.get('carwidth', 65.0),
                'carheight': request.form.get('carheight', 54.0),
                'curbweight': request.form.get('curbweight', 2500),
                'enginesize': request.form.get('enginesize', 120),
                'boreratio': request.form.get('boreratio', 3.3),
                'stroke': request.form.get('stroke', 3.3),
                'compressionratio': request.form.get('compressionratio', 9.0),
                'horsepower': request.form.get('horsepower', 100),
                'peakrpm': request.form.get('peakrpm', 5200),
                'citympg': request.form.get('citympg', 25),
                'highwaympg': request.form.get('highwaympg', 30),
                
                # Categorical features
                'fueltype': request.form.get('fueltype', 'gas'),
                'aspiration': request.form.get('aspiration', 'std'),
                'doornumber': request.form.get('doornumber', 'four'),
                'carbody': request.form.get('carbody', 'sedan'),
                'drivewheel': request.form.get('drivewheel', 'fwd'),
                'enginelocation': request.form.get('enginelocation', 'front'),
                'enginetype': request.form.get('enginetype', 'ohc'),
                'cylindernumber': request.form.get('cylindernumber', 'four'),
                'fuelsystem': request.form.get('fuelsystem', 'mpfi'),
                'Brand': request.form.get('Brand', 'toyota'),
                'Brand_category': request.form.get('Brand_category', 'Mid Range')
            }
            
            # Get brand average price based on selected brand
            if df is not None and 'Brand' in user_input:
                brand_avg = df[df['Brand'] == user_input['Brand']]['brand_avg_price'].mean()
                user_input['brand_avg_price'] = brand_avg
            else:
                user_input['brand_avg_price'] = df['brand_avg_price'].mean() if df is not None else 15000
            
            # Prepare features for prediction
            input_features = prepare_input_features(user_input)
            
            if input_features is not None and model is not None:
                # Make prediction
                predicted_price = model.predict(input_features)[0]
                prediction = {
                    'price': f"${predicted_price:,.2f}",
                    'formatted_price': f"${predicted_price:,.0f}",
                    'raw_price': predicted_price,
                    'user_input': user_input
                }
            else:
                error = "Model not loaded properly. Please try again."
                
        except Exception as e:
            error = f"Error making prediction: {str(e)}"
    
    return render_template('predict.html', 
                         options=options, 
                         prediction=prediction, 
                         error=error)

@app.route('/analyze')
def analyze():
    """Analysis results page"""
    global df
    
    if df is None:
        df = load_and_preprocess_data()
    
    if df is not None:
        # Basic statistics
        stats = {
            'total_cars': len(df),
            'avg_price': f"${df['price'].mean():,.2f}",
            'min_price': f"${df['price'].min():,.2f}",
            'max_price': f"${df['price'].max():,.2f}",
            'brands_count': df['Brand'].nunique(),
            'columns': list(df.columns)
        }
        
        # Create plots
        plot1 = create_brand_distribution_plot()
        plot2 = create_price_distribution_plot()
        plot3 = create_correlation_plot()
        
        return render_template('result.html', 
                             stats=stats, 
                             plot1=plot1, 
                             plot2=plot2,
                             plot3=plot3,
                             table_head=df.head(10).to_html(classes='table table-striped', index=False))
    else:
        return render_template('result.html', error="Failed to load data")

def create_brand_distribution_plot():
    """Create brand distribution plot"""
    plt.figure(figsize=(12, 8))
    data = df['Brand']
    sns.countplot(y=data, order=data.value_counts().index)
    plt.title('Brand Distribution')
    plt.xlabel('Count')
    plt.ylabel('Brand')
    
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return plot_url

def create_price_distribution_plot():
    """Create price distribution plot"""
    plt.figure(figsize=(10, 6))
    df['price'].hist(bins=30, color='lightblue', edgecolor='black')
    plt.title('Price Distribution')
    plt.xlabel('Price ($)')
    plt.ylabel('Frequency')
    
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return plot_url

def create_correlation_plot():
    """Create correlation heatmap"""
    plt.figure(figsize=(12, 8))
    numerical_df = df.select_dtypes(include=[np.number])
    corr = numerical_df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
    plt.title('Feature Correlation Heatmap')
    
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return plot_url

# Initialize data and model when app starts
with app.app_context():
    df = load_and_preprocess_data()
    if df is not None:
        train_model()
        print("✅ Data loaded and model trained successfully!")
        print(f"📊 Dataset shape: {df.shape}")
        print(f"🏷️ Available brands: {len(df['Brand'].unique())}")
    else:
        print("❌ Failed to load data")

if __name__ == '__main__':
    try:
        port = find_available_port(5000, 5010)
        print(f"🚀 Starting Car Price Analysis on http://localhost:{port}")
        print("📊 Application is running...")
        print("🎯 Visit /predict to estimate car prices")
        print("📈 Visit /analyze to see data analysis")
        print("🛑 Press Ctrl+C to stop the server")
        app.run(debug=True, host='0.0.0.0', port=port)
    except Exception as e:
        print(f"Error starting server: {e}")