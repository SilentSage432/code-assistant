from flask import Flask, request, jsonify, render_template
import pylint.lint
from io import StringIO
import sys
import tempfile

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_code():
    data = request.json
    code = data.get('code')
    lang = data.get('language')

    if lang == 'python':
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py', mode='w') as temp:
            temp.write(code)
            temp.flush()
            output = StringIO()
            sys.stdout = output
            pylint.lint.Run(['--msg-template={msg}', '-sn', temp.name], exit=False)
            sys.stdout = sys.__stdout__
            result = output.getvalue().strip()
            return jsonify({'feedback': result or 'No issues found!'})

    elif lang == 'html':
        # Placeholder feedback for HTML analysis
        if '<html' in code.lower():
            return jsonify({'feedback': '✅ HTML structure detected. No critical issues found.'})
        else:
            return jsonify({'feedback': '⚠️ Missing <html> tag or improper structure.'})

    elif lang == 'javascript':
        # Placeholder feedback for JS analysis
        if 'function' in code:
            return jsonify({'feedback': '✅ Function declaration found. Looks good for now.'})
        else:
            return jsonify({'feedback': '⚠️ No function found. JS might be incomplete or unstructured.'})

    else:
        return jsonify({'feedback': '⚠️ Language not supported yet.'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
