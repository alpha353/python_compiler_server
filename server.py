from flask import Flask, request, jsonify
import io
import sys


app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_code():
    # Get the Python code from the request
    code = request.json.get('code', '')
    # Redirect stdout to capture print statements
    output = io.StringIO()
    sys.stdout = output

    try:
        # Execute the Python code
        exec_globals = {}
        exec(code, exec_globals)
        # Get the output
        result = output.getvalue()
        return jsonify({'output': result if result else "No output produced"})
    except Exception as e:
        # Return any syntax or runtime errors
        return jsonify({'error': str(e)})
    finally:
        # Restore stdout
        sys.stdout = sys.__stdout__
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
