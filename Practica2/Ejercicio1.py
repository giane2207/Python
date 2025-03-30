import this

zen_text = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

#Convierto el zen en lista separados por oracion
zen_text = zen_text.split('.\n')
vocales = 'aeiou'
zen_con_vocales = []

for oracion in zen_text:
    # Separo la oracion en palabras
    palabras = oracion.split()
    if (palabras[1][0].lower() in vocales):
        zen_con_vocales.append(oracion)

print(zen_con_vocales)