# coding: utf-8

from horoscope import times, advices, promises

def generate_page(head, body):
	page = f"<html>{head}{body}</html>"
	return page

def generate_head(title):
	head = f"""<head>
	<meta charset='utf-8'>
	<title>{title}</title>
	</head>"""
	return head

def generate_body(header, paragraphs):
    body = f"<h1>{header}</h1><img src='gemini.png' width='100'/>"
    
    body = body + "<ol>"
    for key in paragraphs:
        body = f"{body} <li>{key}</li>"
        for entry in paragraphs[key]:
            body = f"{body}<ul><li>{entry}</li></ul>"
        body = body + "&nbsp"
    body = body + "</ol>"

    body = f"{body}&nbsp<a href='index.html'> На главную </a>"
    return f"<body>{body}</body>"

def save_page(title, header, paragraphs, output="about.html"):
	fp = open(output, "w", encoding="utf-8")
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header, paragraphs=paragraphs)
		)
	print(page, file=fp)
	fp.close()

save_page(
    title="О реализации",
    header="О чем все это",
    paragraphs={'Времена дня:':times, 'Советы:': advices, 'Предсказания:': promises},
    )