# En enkel liste med trafikkmeldinger
trafikkmeldinger = [
    {'by': 'Oslo', 'alvorlighetsgrad': 'høy', 'beskrivelse': 'lørdag 10c'},
    {'by': 'Bergen', 'alvorlighetsgrad': 'moderat', 'beskrivelse': 'lørdag 13c'},
    {'by': 'Trondheim', 'alvorlighetsgrad': 'lav', 'beskrivelse': 'lørdag 8c'},
    {'by': 'Vega', 'alvorlighetsgrad': 'lav', 'beskrivelse': 'lørdag 9c'},
]

# Funksjon som henter og filtrerer meldinger basert på args og kwargs
def hent_meldinger(*args, **kwargs):
    resultater = []
    
    for melding in trafikkmeldinger:
        # Sjekker *args for å filtrere meldinger basert på ord i beskrivelsen
        passer = True
        for ord in args:
            if ord not in melding['beskrivelse']:
                passer = False
                break
        
        # Sjekker **kwargs for å filtrere på by eller alvorlighetsgrad
        for key, value in kwargs.items():
            if melding.get(key) != value:
                passer = False
                break
                
        if passer:
            resultater.append(melding)
    
    return resultater

# Enkel funksjon for å vise meldingene
def vis_meldinger(meldinger):
    for melding in meldinger:
        print(f"By: {melding['by']}, Alvorlighetsgrad: {melding['alvorlighetsgrad']}")
        print(f"Beskrivelse: {melding['beskrivelse']}\n")

# Eksempler på bruk
print("Henter meldinger fra Oslo med alvorlighetsgrad 'høy':")
meldinger = hent_meldinger(alvorlighetsgrad='høy', by='Oslo')
vis_meldinger(meldinger)

print("Henter meldinger som inneholder ordet 'Kø':")
meldinger = hent_meldinger('Kø')
vis_meldinger(meldinger)
