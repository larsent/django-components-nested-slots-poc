from django_components import component


@component.register("example")
class Example(component.Component):
    template_name = "example.html"

    def get_context_data(self):
        return {}
