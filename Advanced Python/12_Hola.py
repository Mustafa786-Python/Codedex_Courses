def translator(language):
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }

    def traslate_word(word):
        return translations[language][word]

    return traslate_word


translate_to_spanish = translator('spanish')
print(translate_to_spanish('goodbye'))  # Output: hola
