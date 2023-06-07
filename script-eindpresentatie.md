# Schetsing
We zitten allemaal terug in de laatste graad van het middelbaar onderwijs. Om bewust te worden van wetenschappelijk onderzoek, krijgen wij tijdens onze STEM-vakken een wetenschappelijk artikel voorgeschoteld. Een opdracht begrijpend lezen kan ons doen inzien waarom wetenschappelijk onderzoek wordt gedaan, maar ook om ons actueel te houden van de laatste wetenschappelijke inzichten. Deze structuur herkennen we ongetwijfeld, maar wat als ik nu een aanpassing laat maken aan de tekst.

Wat ik jullie nu toon is geen optisch fenomeen, maar wel iets waar scholieren in het middelbaar onderwijs mee kunnen te maken hebben. Deze simulatie benadrukt hoe moeilijk het begrijpend lezen van deze artikelen kan worden voor scholieren met dyslexie. Onderzoeken wijzen uit hoe de digitale weergave van deze teksten kan verbeterd worden. Zo kan het lettertype naar een sans-serif font aangepast worden, het lettertype kunnen we opschalen naar 15pt en de achtergrondkleur kan aangepast worden om deze scholieren een aangenamere leeservaring aan te bieden. Toch blijft de tekst in het wetenschappelijk artikel een obstakel voor alle scholieren in het middelbaar onderwijs. Onderzoeken wijzen uit dat de benodigde geletterdheid van deze teksten alsmaar stijgt, waardoor een steeds groter percentage de grip op deze materie verliest.

Bestaande toepassingen kunnen dit reeds al, maar het artikel beschikt nog steeds over wetenschappelijk jargon, lange zinnen die over meerdere lijnen kunnen spreiden, meerlettergreperige woorden of complexe zinsyntaxen. Hiervoor bestaat er wel al een oplossing. Zo kunnen leerkrachten wetenschappelijke artikelen vereenvoudigen op maat van deze scholieren. Zij kunnen de tekstinhoud van een wetenschappelijk artikel overnemen en in een Word-document de opmaak aanpassen, maar ook de tekst herschrijven volgens de achtergrondkennis van de leerlingen. 

Hiervoor kunnen zij drie aanpassingen maken:

1. Lexicale aanpassingen kunnen leerkrachten doen door de moeilijke woorden in de tekst te vervangen door een eenvoudiger synoniem. Als er geen eenvoudiger synoniem staat, kan de leerkracht de zin herschrijven tot die een in-line betekenis bevat. Ondersteunend hierop kan de leerkracht ook een woordenlijst schrijven dat alles regelt.

Moeilijke woordenschat kan vervangen worden. Echter moeten we rekening houden met de doelgroep. Jargon dat reeds gekend is, behoort nog steeds tot te kennen leerstof en deze moeten blijven staan. Bij MTS komt een didactisch aspect bij kijken. Zo moet dergelijk prototype enkel ondersteuning bieden en geen vervangende tekst genereren.

Er is een bewezen effect van MTS voor zowel scholieren met dyslexie als scholieren zonder dyslexie. Al is er geen gekend percentage over hoeveel leerkrachten dit doen, toch  

Allereerst kijken we naar de verschillende toepassingen. Zo leent de overheid vijf softwarepakketten uit. Van deze vijf staan stil bij Kurzweil, Sprint en Alinea. Deze pakketten zijn op maat gemaakt voor scholieren met dyslexie door luistersoftware aan te reiken in een aanpasbare omgeving. Zo kunnen scholieren de lettertype- en spatiëring aanpassen naar hun wens. Deze pakketten bieden geen MTS-technieken aan, buiten het genereren van woordenlijsten. De tekst blijft zoals voordien.

Online vinden we wel weer andere toepassingen terug.

Huidige taalmodellen en toepassingen kunnen teksten vereenvoudigen, maar deze toepassingen Dit onderzoek kan vrijwel een grote groep in het onderwijs baten. 


# Prototype

Het prototype kan twee doelgroepen baten. Allereerst zijn er scholieren die een tool willen waar zij aanpassingen kunnen maken aan de tekst. Anderzijds leerkrachten die een gegenereerde tekst willen laten maken voor een specifieke doelgroep. Om scholieren met dyslexie extra te kunnen ondersteunen, biedt het prototype opmaakopties aan zowel binnen de site, als in het gegenereerde document.

Deel van de prompts

Temperature zorgt ervoor dat het taalmodel binnen de perken wordt gehouden. Zo wijkt het taalmodel niet van de oorspronkelijke context af. Daarnaast zorgt de top-p waarde voor een 

## Scholierencomponent

Het scholierencomponent combineert de kracht van het GPT-3 talenmodel, met de intuïtiveit uit toepassingen zoals Scispace. Scholieren kunnen namelijk tekst markeren en deze vervolgens laten vereenvoudigen. Bij de vereenvoudiging kunnen scholieren ook kiezen of deze tekst in doorlopende tekst moet; of per opsomming. De opsomming is handiger om een snel overzicht te hebben van de gemarkeerde tekst. Naast een ingebakken prompt, kunnen scholieren ook zelf een prompt schrijven. Zo kunnen ze een vraag stellen aan het taalmodel om hen te ondersteunen bij het begrijpen lezen. Om deze scholieren verder te ondersteunen, kan het prototype ook een woordenlijst opbouwen na een handmatige selectie van kernwoorden. Het prototype biedt ondersteuning aan, zonder didactische waarden van de scholier af te nemen.

Kortom kunnen ontwikkelaars met vrij basiskennis van JavaScript en Python de bestaande toepassingen recreëeren.

## Lerarencomponent

Naast een ondersteunende tool, kan het prototype ook de werkdruk bij leerkrachten verminderen. Voordien moesten leerkrachten handmatig eerst de tekst doornemen

Enkel wordt er één prompt voor het volledige document gebruikt. Een volgende iteratie van het prototype zou per zin, per paragraaf of per hoofdstuk een prompt moeten krijgen. 

Alle tekstinhoud moet omgevormd worden naar een document dat scholieren kunnen terugkrijgen. Daardoor kunnen ontwikkelaars gebruikmaken van Pandoc. Alle vereenvoudigde tekstinhoud wordt naar een markdown-bestand uitgeschreven, die vervolgens naar een pdf of word document wordt omgezet. Met Pandoc kan het prototype de uitvoertekst in een personaliseerbaar formaat aanreiken. Wel is de opmaak beperkt bij Word / docx-bestanden. PDF's zijn opgebouwd met de Xelatex-engine en daardoor zijn alle opmaakopties om scholieren met dyslexie te helpen, parameteriseerbaar. Werken met pandoc laat de deur ook open om vereenvoudigde wetenschappelijke artikelen te genereren in epub (of eBook) formaat en eventueel slides genereren.


# Conclusie

Het prototype kan een ondersteunend middel aanbieden voor scholieren met dyslexie dankzij een carte blanche functionaliteit. Scholieren kunnen eender welke aanpassing maken op de oorspronkelijke tekst, vooral gericht op de vereenvoudiging ervan. Hoewel Pandoc en GPT-3 een mooie start kunnen aanreiken voor gepersonaliseerde ATS, toch is het taalmodel niet 100% zeker voor welke doelgroep ATS moet uitgevoerd worden. Daarnaast wordt enkel de tekstinhoud bekeken. Een verder onderzoek met GPT-4 moet aanduiden of dit taalmodel de doelgroep beter kan inschatten. 

Voor betere gepersonaliseerde ATS, kunnen volgende onderzoeken kijken naar one-shot summaries, door de eindgebruiker een paragraaf te laten schrijven waarop het taalmodel zich kan baseren, of door het opschalen naar GPT-4 dat over meer parameters beschikt.

Daarnaast houdt het prototype enkel rekening met de tekstinhoud en niet met afbeeldingen. De volgende iteratie van het GPT-taalmodel is wel in staat om afbeeldingen te interpreteren en te genereren. Zo kan een volgend onderzoek stilstaan bij de capabiliteiten van GPT-4 bij het interpreteren van grafieken of gevisualiseerd cijfermateriaal. Daarnaast kan het mogelijks aanschouwlijkheid voor de gebruiker aanbieden door 