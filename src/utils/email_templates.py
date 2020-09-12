from django import template


def single_verse_template(context):
    verse_template = template.Template('<html><head><style> </style></head>'
                                       '<body>'
                                       '<p style="font-size: 20pt">{{arabic}}</p>'
                                       '<p class="translation">{{english}}</p>'
                                       '<audio id="ayah-audio" width="1" controls="" preload="none">'
                                       '<source src="http://cdn.alquran.cloud/media/audio/ayah/ar.alafasy/{{ayah}}/high" type="audio/mpeg"/>'
                                       '<p>? Listen :<a href="http://cdn.alquran.cloud/media/audio/ayah/ar.alafasy/{{ayah}}/high">Bismillah</a></p>'
                                       '</audio>'
                                       '</body></html>')
    return verse_template.render(context)
