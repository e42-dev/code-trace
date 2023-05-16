import sys
from read_program_details import *

html_template_part_1 = """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
    <title>{title}</title> 
    <script type="text/javascript" src="{js_loc}"></script> 
    <link type="text/css" rel="stylesheet" href="{css_loc}"></link>
"""
html_template_part_2 = """
    <style type='text/css'>
     ol.interactivities > li {
       list-style: none;
       margin-bottom: 2em;
     }
     .problemheading {
       font-size: 1.4em;
       font-weight: bold;
       font-family: monospace;
       border-top: thin dotted black;
       padding-top: 0.4em;
     }
     body {
       margin-left: 2em;
       margin-right: 2em;
       overflow-y: visible;
       font-size: x-large;
     }
    </style>
  </head>
"""
html_template_part_3 = """ 
  <body>
    <ol class='interactivities' id='interactivities'>
      <li title='{walkthrough_id}' id='{walkthrough_id}'>
        <div class='hc-included'>
          <div>
            <p>{explaination}</p>
            <div class='e42_walkthrough'>
              <pre>
{code}
            </pre>
            <table style="font-size:x-large">
              <tr>
{variables}
              </tr>
            </table>
              <script type='text/javascript'>//<![CDATA[
{walkthrough}
              //]]> </script> 
            </div>
          </div>
        </div>
      </li>
    </ol>
    <div class='vstreport'></div>
  </body>
</html>"""

file_name = sys.argv[1]
title, walkthrough_id, explaination, code, variables, walkthrough = get_details_from_file(file_name)

variables_list = variables.split(" ")
variables_html = ""
for variable in variables_list:
  variables_html += "<th>" + variable + "</th>\n"

html = html_template_part_1.format(title=title, js_loc="https://e42.dev/c/assets/scripts/e42_all_min.js", css_loc="https://e42.dev/c/assets/css/e42_all_min.css")
html = html + html_template_part_2
html = html + html_template_part_3.format(walkthrough_id= walkthrough_id, explaination=explaination, code=code, variables=variables_html, walkthrough=walkthrough)

print(html)