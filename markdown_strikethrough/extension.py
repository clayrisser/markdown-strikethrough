from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
import re

def makeExtension(configs=None):
    if configs is None:
        return StrikethroughExtension()

class StrikethroughExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        postprocessor = StrikethroughPostprocessor(md)
        md.postprocessors.add('strikethrough', postprocessor, '>raw_html')

class StrikethroughPostprocessor(Postprocessor):
    """
    adds strikethrough
    """

    pattern = re.compile(r'~~(((?!~~).)+)~~')

    def run(self, html):
        return re.sub(self.pattern, self.convert, html)

    def convert(self, match):
        return '<del>' + match.group(1) + '</del>'
