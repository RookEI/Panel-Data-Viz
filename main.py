import panel as pn
pn.config.sizing_mode="stretch_width"
header = pn.pane.Markdown("""# Autoreload Flag
                          
The '--autoreload' flag enables high speed
reloads when you save the file

Use it via

'''bash
panel serve name_of_file.py --autoreload
'''

""")

section = pn.Spacer(
    height=300,
    sizing_mode="stretch_width",
    background="green"   
)

app = pn.template.FastListTemplate(
    title="panel - Autoreload",
    main=[header, section]
)

app.servable()