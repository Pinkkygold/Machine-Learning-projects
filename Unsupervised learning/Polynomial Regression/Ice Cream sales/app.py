from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error
import io
import base64
import os
import traceback

app = Flask(__name__)

# Load and prepare data
def load_data():
    try:
        df = pd.read_csv('Ice_cream_selling_data.csv')
        print(f"Data loaded successfully: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        # Return sample data if file not found
        return pd.DataFrame({
            'Temperature (°C)': [20, 25, 30, 15, 35, 10, 40],
            'Ice Cream Sales (units)': [50, 75, 100, 30, 120, 25, 150]
        })

def train_polynomial_model(degree=2):
    """Train polynomial regression model"""
    df = load_data()
    
    x = df[['Temperature (°C)']]
    y = df['Ice Cream Sales (units)']
    
    # Split the data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    # Create polynomial features
    poly = PolynomialFeatures(degree=degree, include_bias=True)
    x_train_poly = poly.fit_transform(x_train)
    x_test_poly = poly.transform(x_test)
    
    # Train model
    model = LinearRegression()
    model.fit(x_train_poly, y_train)
    
    # Make predictions
    y_pred = model.predict(x_test_poly)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    return {
        'model': model,
        'poly': poly,
        'x_train': x_train,
        'y_train': y_train,
        'x_test': x_test,
        'y_test': y_test,
        'y_pred': y_pred,
        'mse': mse,
        'r2': r2,
        'degree': degree,
        'x_full': x,
        'y_full': y
    }

def create_plot(model_data, prediction_temp=None):
    """Create interactive plot with polynomial regression"""
    try:
        plt.figure(figsize=(12, 8))
        
        # Extract data
        x_full = model_data['x_full']
        y_full = model_data['y_full']
        model = model_data['model']
        poly = model_data['poly']
        degree = model_data['degree']
        
        # Create smooth curve for polynomial regression
        x_grid = np.linspace(x_full.min(), x_full.max(), 100).reshape(-1, 1)
        x_grid_poly = poly.transform(x_grid)
        y_grid_pred = model.predict(x_grid_poly)
        
        # Plot actual data
        plt.scatter(x_full, y_full, color='blue', alpha=0.7, s=60, label='Actual Data', edgecolors='black')
        
        # Plot polynomial regression line
        plt.plot(x_grid, y_grid_pred, color='red', linewidth=3, label=f'Polynomial Regression (Degree {degree})')
        
        # Plot prediction point if provided
        if prediction_temp is not None:
            prediction_data = [[prediction_temp]]
            prediction_poly = poly.transform(prediction_data)
            prediction_sales = model.predict(prediction_poly)[0]
            
            plt.scatter([prediction_temp], [prediction_sales], color='green', s=200, 
                       marker='*', edgecolors='black', linewidth=2, 
                       label=f'Prediction: {prediction_temp}°C → {prediction_sales:.0f} units')
            
            plt.annotate(f'{prediction_sales:.0f} units', 
                        xy=(prediction_temp, prediction_sales),
                        xytext=(prediction_temp, prediction_sales + 5),
                        ha='center', fontsize=12, fontweight='bold',
                        bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
        
        plt.xlabel('Temperature (°C)', fontsize=14, fontweight='bold')
        plt.ylabel('Ice Cream Sales (units)', fontsize=14, fontweight='bold')
        plt.title('Ice Cream Sales vs Temperature (Polynomial Regression)', fontsize=16, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=12)
        
        # Convert plot to base64
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight', dpi=100, facecolor='white')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        
        return plot_url
    except Exception as e:
        print(f"Error creating plot: {e}")
        return ""

@app.route('/')
def index():
    try:
        # Load data for statistics
        df = load_data()
        
        # Train polynomial model
        model_data = train_polynomial_model(degree=2)
        
        # Create initial plot
        plot_url = create_plot(model_data)
        
        # Calculate statistics
        stats = {
            'total_records': len(df),
            'avg_temperature': float(df['Temperature (°C)'].mean()),
            'avg_sales': float(df['Ice Cream Sales (units)'].mean()),
            'max_temp': float(df['Temperature (°C)'].max()),
            'min_temp': float(df['Temperature (°C)'].min()),
            'max_sales': float(df['Ice Cream Sales (units)'].max()),
            'min_sales': float(df['Ice Cream Sales (units)'].min()),
            'correlation': float(df['Temperature (°C)'].corr(df['Ice Cream Sales (units)']))
        }
        
        # Model performance
        performance = {
            'r2': model_data['r2'],
            'mse': model_data['mse'],
            'degree': model_data['degree'],
            'r2_percentage': model_data['r2'] * 100
        }
        
        return render_template('index.html', 
                             plot_url=plot_url, 
                             stats=stats, 
                             performance=performance,
                             data=df.to_dict('records'))
    except Exception as e:
        error_message = f"Error in index route: {str(e)}\n{traceback.format_exc()}"
        print(error_message)
        return f"<h1>Application Error</h1><pre>{error_message}</pre>", 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        temperature = float(request.json['temperature'])
        degree = int(request.json.get('degree', 2))
        
        # Train model with specified degree
        model_data = train_polynomial_model(degree=degree)
        model = model_data['model']
        poly = model_data['poly']
        
        # Make prediction
        new_data = [[temperature]]
        new_data_poly = poly.transform(new_data)
        prediction = model.predict(new_data_poly)[0]
        
        # Create plot with prediction point
        plot_url = create_plot(model_data, prediction_temp=temperature)
        
        return jsonify({
            'success': True,
            'temperature': temperature,
            'predicted_sales': round(prediction, 2),
            'degree': degree,
            'r2': model_data['r2'],
            'mse': model_data['mse'],
            'r2_percentage': model_data['r2'] * 100,
            'plot_url': plot_url
        })
    except Exception as e:
        error_message = f"Error in predict route: {str(e)}\n{traceback.format_exc()}"
        print(error_message)
        return jsonify({'success': False, 'error': str(e)})

@app.route('/update_model', methods=['POST'])
def update_model():
    try:
        degree = int(request.json['degree'])
        
        # Train new model with updated degree
        model_data = train_polynomial_model(degree=degree)
        plot_url = create_plot(model_data)
        
        return jsonify({
            'success': True,
            'degree': degree,
            'r2': model_data['r2'],
            'mse': model_data['mse'],
            'r2_percentage': model_data['r2'] * 100,
            'plot_url': plot_url
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/data')
def api_data():
    df = load_data()
    return jsonify(df.to_dict('records'))

@app.route('/api/stats')
def api_stats():
    df = load_data()
    stats = {
        'total_records': len(df),
        'temperature_stats': {
            'mean': float(df['Temperature (°C)'].mean()),
            'std': float(df['Temperature (°C)'].std()),
            'min': float(df['Temperature (°C)'].min()),
            'max': float(df['Temperature (°C)'].max())
        },
        'sales_stats': {
            'mean': float(df['Ice Cream Sales (units)'].mean()),
            'std': float(df['Ice Cream Sales (units)'].std()),
            'min': float(df['Ice Cream Sales (units)'].min()),
            'max': float(df['Ice Cream Sales (units)'].max())
        },
        'correlation': float(df['Temperature (°C)'].corr(df['Ice Cream Sales (units)']))
    }
    return jsonify(stats)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "message": "Server is running"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)