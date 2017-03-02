# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2

html = """
	<h1>HEllo I'm Nausica. Check out my artwork</h1>
	<img src='https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwitnZfE48rRAhWGRiYKHRQlDYMQjRwIBQ&url=https%3A%2F%2Fvine.co%2Fu%2F941902279374700544&psig=AFQjCNGxNDKASRtn3mc0RD7zaj1xZeKEYw&ust=1484797413053524'>
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(html)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
