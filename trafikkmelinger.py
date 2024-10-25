# En enkel liste med trafikkmeldinger
trafikkmeldinger = [
    {'by': 'Oslo', 'alvorlighetsgrad': 'høy', 'beskrivelse': 'Ulykke på E6'},
    {'by': 'Bergen', 'alvorlighetsgrad': 'moderat', 'beskrivelse': 'Veiarbeid på E39'},
    {'by': 'Trondheim', 'alvorlighetsgrad': 'lav', 'beskrivelse': 'Kø på vei 705'},
    {'by': 'Vega', 'alvorlighetsgrad': 'lav', 'beskrivelse': 'Båt gikk i dag'},
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
