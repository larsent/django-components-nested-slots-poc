from django_components import component


@component.register("flat_example")
class FlatExample(component.Component):
    template_name = "flat_example_component.html"

    def get_context_data(self):
        return {}
