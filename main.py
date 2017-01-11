import webapp2
import os
import jinja2

template_dir = os.path.dirname(__file__)
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template("index.html")
        rendered_template = t.render()
        self.response.out.write(rendered_template)
        
    def post(self):
        my_string = self.request.get("text")
        final_string = ""
        for char in my_string:
            if ord(char) in range(65, 92):
                if 91 - ord(char) > 13:
                    final_string += chr(ord(char) + 13)
                else:
                    final_string += chr(65 + (13 - (91 - ord(char) + 1)))
            if ord(char) in range(97, 124):
                if 123 - ord(char) > 13:
                    final_string += chr(ord(char) + 13)
                else:
                    final_string += chr(97 + (13 - (123 - ord(char) + 1)))
        t = jinja_env.get_template("index.html")
        rendered_template = t.render(ciphered = final_string)
        self.response.out.write(rendered_template)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
