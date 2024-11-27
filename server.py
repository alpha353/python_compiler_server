from flask import Flask, request, jsonify
import io
import sys

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    output = io.StringIO()
    sys.stdout = output

    try:
        exec_globals = {}
        exec(code, exec_globals)
        result = output.getvalue()
        return jsonify({'output': result if result else "No output produced"})
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        sys.stdout = sys.__stdout__
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
