from ..factory.RuntimeSourceTemplate import RuntimeSourceTemplate

class RuntimeSourceTemplateDocker(RuntimeSourceTemplate):
    
    def __init__(self):
        self.__template =  """
FROM {{ image.name }}:{{ image.tag }}

{% if env %}{% for key, value in env.export.iteritems() %}ENV {{ key }} {{ value }}
{% endfor %}{% endif %}
{% if copy %}COPY {{ copy.dfrom }} {{ copy.dto }}{% endif %}
{% if run %}
RUN {% for command in run.commands %}{{ command }}{% if not loop.last %} && \ \n    {% endif %}{% endfor %} 
{% endif %}
CMD {{ cmd.command }}"""

    
    @property
    def template(self):
        return self.__template

