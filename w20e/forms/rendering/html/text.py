from templates import get_template
from w20e.forms.rendering.interfaces import IControlRenderer
from zope.interface import implements


class TextRenderer:

    implements(IControlRenderer)

    def render(self, renderer, form, renderable, out, **kwargs):

        fmtmap = renderer.createFormatMap(form, renderable, **kwargs)

        print >> out, get_template("text")(
            control=renderable,
            extra_classes=fmtmap['extra_classes']
            )
