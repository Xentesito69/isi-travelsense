import random

def generar_datos_masivos():
    """Genera cerca de 600 destinos y sus eventos asociados."""
    
    # Estructura: Regi├│n -> Pa├¡s -> Lista de (Ciudad, Descripci├│n, Clima)
    lugares = {
        "Europa": {
            "Espa├▒a": [
                ("Madrid", "Capital cultural, museos y vida nocturna", "Variable"),
                ("Barcelona", "Arquitectura modernista y costa mediterr├ínea", "H├║medo y suave"),
                ("Valencia", "Ciudad de las Artes, playa y paella", "H├║medo y c├ílido"),
                ("Sevilla", "Flamenco, tapas y arquitectura morisca", "Muy caluroso"),
                ("Zaragoza", "Legado romano, el Pilar y tapas", "Ventoso"),
                ("M├ílaga", "Costa del Sol, museos Picasso y espetos", "Mediterr├íneo"),
                ("Murcia", "Huerta de Europa y catedral barroca", "Muy caluroso"),
                ("Palma de Mallorca", "Playas cristalinas y catedral g├│tica", "Mediterr├íneo"),
                ("Las Palmas", "Playas y clima primaveral todo el a├▒o", "Suave"),
                ("Bilbao", "Museo Guggenheim y pintxos de primer nivel", "Oce├ínico"),
                ("Alicante", "Castillo de Santa B├írbara y playas doradas", "Mediterr├íneo"),
                ("C├│rdoba", "Mezquita-Catedral y patios de flores", "Caluroso"),
                ("Valladolid", "Cuna del castellano y buen vino", "Continental"),
                ("Vigo", "Puerto mar├¡timo, marisco y luces", "Oce├ínico"),
                ("Gij├│n", "Costa asturiana, sidra y romanismo", "Oce├ínico"),
                ("Hospitalet de Llobregat", "Ciudad de contrastes y ferias", "Mediterr├íneo"),
                ("Vitoria-Gasteiz", "Capital verde europea y anillo verde", "Oce├ínico"),
                ("A Coru├▒a", "Torre de H├®rcules y paseo mar├¡timo", "Oce├ínico"),
                ("Granada", "La Alhambra y maravillas nevadas", "Continental"),
                ("Elche", "Palmeral Patrimonio de la Humanidad", "Mediterr├íneo"),
                ("Oviedo", "Prerrom├ínico asturiano y dulces", "Oce├ínico"),
                ("Santa Cruz de Tenerife", "Carnavales y clima atl├íntico", "Suave"),
                ("Cartagena", "Teatro romano y puerto de culturas", "Mediterr├íneo"),
                ("Terrassa", "Masia freixa y pasado industrial", "Mediterr├íneo"),
                ("Jerez de la Frontera", "Motos, vino y caballos", "Caluroso"),
                ("Sabadell", "Modernismo e historia textil", "Mediterr├íneo"),
                ("M├│stoles", "Parques y proximidad capitalina", "Variable"),
                ("Alcal├í de Henares", "Universidad hist├│rica y Cervantes", "Variable"),
                ("Pamplona", "Sanfermines y murallas centenarias", "Continental"),
                ("Almer├¡a", "Alcazaba e historias de cine", "Des├®rtico"),
                ("Fuenlabrada", "Vanguardia en el sur de Madrid", "Variable"),
                ("Legan├®s", "Zonas verdes y vida universitaria", "Variable"),
                ("Donostia/San Sebasti├ín", "Playa de la Concha y estrellas Michelin", "Oce├ínico"),
                ("Getafe", "Cerro de los ├üngeles y aviaci├│n", "Variable"),
                ("Burgos", "Catedral g├│tica y evoluci├│n humana", "Continental"),
                ("Santander", "Bah├¡a impresionante y Palacio Magdalena", "Oce├ínico"),
                ("Albacete", "Cuchiller├¡a y ferias tradicionales", "Variable"),
                ("Castell├│n de la Plana", "El Fadr├¡ y clima naranja", "Mediterr├íneo"),
                ("Logro├▒o", "Calle Laurel y capital del Rioja", "Continental"),
                ("Badajoz", "Alcazaba y frontera multicultural", "Caluroso"),
                ("Salamanca", "Ciudad universitaria dorada y Plaza Mayor", "Continental"),
                ("Huelva", "Lugares colombinos y gamba blanca", "Suave"),
                ("Marbella", "Lujo, Puerto Ban├║s y playa", "Mediterr├íneo"),
                ("Lleida", "Seu Vella y huerta frutal", "Continental"),
                ("Tarragona", "Tarraco romana y Costa Dorada", "Mediterr├íneo"),
                ("Le├│n", "Barrio h├║medo y catedral g├│tica", "Continental"),
                ("C├ídiz", "La Tacita de Plata y carnavales", "H├║medo"),
                ("Ja├®n", "Capital del Santo Reino y olivares", "Caluroso"),
                ("Ourense", "Termas milenarias y puentes", "Oce├ínico"),
            ],
            "Francia": [
                ("Par├¡s", "La ciudad del amor, arte y moda", "Templado"),
                ("Marsella", "Puerto vital y herencia mediterr├ínea", "Mediterr├íneo"),
                ("Lyon", "Capital gastron├│mica y cuna del cine", "Continental"),
                ("Toulouse", "La ciudad rosa y la aerona├║tica", "Suave"),
                ("Niza", "Paseo de los Ingleses y Costa Azul", "Mediterr├íneo"),
                ("Nantes", "M├íquinas de la isla y castillos", "Oce├ínico"),
                ("Montpellier", "Ciudad joven y plazas milenarias", "Mediterr├íneo"),
                ("Estrasburgo", "Capital europea y encanto alsaciano", "Continental"),
                ("Burdeos", "Cuna de los mejores vinos del mundo", "Oce├ínico"),
                ("Lille", "Arquitectura flamenca y cerveza", "Fresco"),
                ("Rennes", "Casas de entramado y breta├▒a", "Oce├ínico"),
                ("Reims", "Capital del champ├ín e historia real", "Continental"),
                ("Le Havre", "Puerto reconstruido patrimonio", "Oce├ínico"),
                ("Saint-├ëtienne", "Ciudad del dise├▒o y la industria", "Continental"),
                ("Tol├│n", "Puerto militar y montes costeros", "Mediterr├íneo"),
                ("Grenoble", "Capital de los alpes franceses", "Alpino"),
                ("Dijon", "Mostaza, b├║hos y vinos de borgo├▒a", "Continental"),
                ("Angers", "Castillo y tapiz del apocalipsis", "Oce├ínico"),
                ("Aix-en-Provence", "Fuentes y paisajes de C├®zanne", "Mediterr├íneo"),
                ("Cannes", "Festival de cine e islas de L├®rins", "Mediterr├íneo")
            ],
            "Italia": [
                ("Roma", "La Ciudad Eterna y ruinas romanas", "Mediterr├íneo"),
                ("Mil├ín", "Moda, Duomo y la ├Ültima Cena", "Continental"),
                ("N├ípoles", "Vesubio, pizza y caos encantador", "Mediterr├íneo"),
                ("Tur├¡n", "Elegancia sabauda y los Alpes", "Continental"),
                ("Palermo", "Mezcla ├írabe-normanda y calles vibrantes", "Mediterr├íneo"),
                ("G├®nova", "Puerto hist├│rico y los Palazzi dei Rolli", "Mediterr├íneo"),
                ("Bolonia", "La Docta, la Gorda y la Roja", "Continental"),
                ("Florencia", "Cuna del Renacimiento y maravillas de arte", "Mediterr├íneo"),
                ("Bari", "San Nicol├ís y rica costa adri├ítica", "Mediterr├íneo"),
                ("Catania", "Piedra de lava y el imponente Etna", "Mediterr├íneo"),
                ("Venecia", "Canales rom├ínticos y arquitectura g├│tica", "H├║medo"),
                ("Verona", "Arena romana y el balc├│n de Julieta", "Continental"),
                ("Mesina", "Estrecho m├¡tico y campanario reloj", "Mediterr├íneo"),
                ("Padua", "Fresco de Giotto y San Antonio", "Continental"),
                ("Trieste", "Caf├®s vieneses y muelle majestuoso", "Ventoso"),
                ("Brescia", "Ruinas romanas y vi├▒edos de Franciacorta", "Continental"),
                ("Parma", "Prosciutto, Parmigiano y Baptisterio", "Continental"),
                ("Tarento", "Dos mares e historia espartana", "Mediterr├íneo"),
                ("Prato", "Historia textil cantucci dulces", "Mediterr├íneo"),
                ("M├│dena", "Aceto bals├ímico, Ferrari y catedral", "Continental"),
                ("Regio de Calabria", "Bronces de Riace y bergamota", "Mediterr├íneo"),
                ("Reggio Emilia", "Bandera tricolor y Parmigiano Reggiano", "Continental"),
                ("Perugia", "Chocolates y murallas etruscas", "Continental"),
                ("R├ívena", "Mosaicos bizantinos espectaculares", "H├║medo"),
                ("Livorno", "Canales fosos y puerto toscano", "Mediterr├íneo")
            ],
            "Alemania": [
                ("Berl├¡n", "Muro antiguo, vanguardia y techno", "Continental"),
                ("Hamburgo", "El inmenso puerto, canales y miniatur", "Oce├ínico"),
                ("M├║nich", "Oktoberfest y coraz├│n de Baviera", "Continental"),
                ("Colonia", "La majestuosa catedral y el Rin", "Templado"),
                ("Fr├íncfort", "El Manhattan europeo y finanzas", "Templado"),
                ("Stuttgart", "Coches de lujo y colinas de vi├▒edos", "Templado"),
                ("D├╝sseldorf", "Moda, Rin y la barra m├ís larga", "Templado"),
                ("Leipzig", "M├║sica cl├ísica y la nueva Berl├¡n", "Continental"),
                ("Dortmund", "F├║tbol pasional e historia industrial", "Templado"),
                ("Essen", "Complejo Zollverein y miner├¡a transformada", "Templado"),
                ("Bremen", "Los m├║sicos del cuento y un hermoso ayuntamiento", "Oce├ínico"),
                ("Dresde", "Florencia del Elba y belleza barroca", "Continental"),
                ("Hannover", "Ferias tecnol├│gicas y jardines reales", "Templado"),
                ("N├║remberg", "Castillo imperial y mercado navide├▒o", "Continental"),
                ("Duisburgo", "Grandes parques paisaj├¡sticos industriales", "Templado"),
                ("Bochum", "Planetario famoso y cuenca del Ruhr", "Templado"),
                ("Wuppertal", "El famoso tren suspendido ├║nico en el mundo", "Templado"),
                ("Bielefeld", "Castillo de Sparrenburg y mito moderno", "Templado"),
                ("Bonn", "Ciudad natal de Beethoven", "Templado"),
                ("M├╝nster", "Capital de la bicicleta y la paz", "Templado")
            ],
            "Reino Unido": [
                ("Londres", "Historia real, cultura moderna y pubs", "Lluvioso"),
                ("Birmingham", "Canales extensos y pasado industrial de oro", "Templado"),
                ("M├ínchester", "Revoluci├│n industrial y epicentro musical", "Lluvioso"),
                ("Glasgow", "Arte victoriano y car├ícter fuerte", "Lluvioso"),
                ("Liverpool", "Los Beatles y la gloria marinera", "Oce├ínico"),
                ("Edimburgo", "Castillo medieval y el festival de Fringe", "Fresco"),
                ("Leeds", "Zonas comerciales victorianas y rica cultura", "Fresco"),
                ("Bristol", "Puente colgante, globos y arte urbano de Banksy", "Suave"),
                ("Sheffield", "Del acero a la ecolog├¡a verde", "Fresco"),
                ("Newcastle", "Siete puentes impresionantes y las Geordies", "Fresco"),
                ("Ayer", "Playas bonitas en el fiordo", "Lluvioso"),
                ("Nottingham", "Robin Hood y cuevas secretas", "Templado"),
                ("Southampton", "Puerto de cruceros y el Titanic", "Moderado"),
                ("Belfast", "Museo del Titanic y los astilleros", "Lluvioso"),
                ("Cardiff", "Castillo central y bah├¡a galesa moderna", "Moderado"),
                ("Aberdeen", "La ciudad de granito brillante", "Fr├¡o"),
                ("Oxford", "Universidad antigua y torres de cuento", "Templado"),
                ("Cambridge", "Tradici├│n universitaria y punting en el r├¡o", "Templado"),
                ("York", "Calles vikingas y la inmensa catedral", "Fresco"),
                ("Bath", "Termas romanas intocables de Jane Austen", "Templado")
            ],
            "Pa├¡ses Bajos": [
                ("├ümsterdam", "Canales, bicicletas y museos mundiales", "Oce├ínico"),
                ("R├│terdam", "Arquitectura moderna y el puerto gigante", "Oce├ínico"),
                ("La Haya", "Corte internacional y sede real", "Oce├ínico"),
                ("Utrecht", "La torre Dom y canales a nivel", "Oce├ínico"),
                ("Eindhoven", "Capital tecnol├│gica e historia de Philips", "Oce├ínico"),
                ("Tilburgo", "Industria textil convertida en arte", "Oce├ínico"),
                ("Groninga", "Ciudad universitaria rebelde y vibrante", "Fresco"),
                ("Almere", "Urbanismo de la nada ganada al mar", "Oce├ínico"),
                ("Breda", "Centro hist├│rico y bosque de pinos", "Oce├ínico"),
                ("Nimega", "La ciudad m├ís antigua con mucha marcha", "Oce├ínico")
            ],
            "Suiza": [
                ("Z├║rich", "Centro financiero global y lago pr├¡stino", "Alpino"),
                ("Ginebra", "Diplomacia relojera y el lago Leman", "Alpino"),
                ("Basilea", "Ciudad tri-fronteriza, museos y Carnaval", "Templado"),
                ("Lausana", "Capital ol├¡mpica y laderas con uvas", "Alpino"),
                ("Berna", "Los osos, Zytglogge y capital medieval", "Alpino"),
                ("Lucerna", "El famoso puente de madera Capilla", "Alpino"),
                ("San Galo", "Abad├¡a Patrimonio de Humanidad", "Fr├¡o"),
                ("Lugano", "Sabor italiano en el lago Suizo", "Templado"),
                ("Friburgo", "Dos idiomas y catedral g├│tica", "Alpino"),
                ("Thun", "Castillo de torres frente al lago", "Alpino")
            ],
            "Pen├¡nsula Balc├ínica y Europa del Este": [
                ("Atenas", "La Acr├│polis y cuna de la democracia", "Mediterr├íneo"),
                ("Sal├│nica", "La segunda ciudad de Grecia con Torre Blanca", "Mediterr├íneo"),
                ("Estambul", "El B├│sforo, mezquitas majestuosas y bazares", "Templado"),
                ("Ankara", "Capital turca y el mausoleo de Ataturk", "Continental"),
                ("Antalya", "Costa turquesa y ruinas antiguas", "Mediterr├íneo"),
                ("Praga", "Ciudad de las 100 torres y encanto m├¡stico", "Continental"),
                ("Brno", "La capital de Moravia y modernismo funcional", "Continental"),
                ("Varsovia", "La Sirena her├│ica resurgida de las cenizas", "Continental"),
                ("Cracovia", "Leyenda del drag├│n y castillos conservados", "Continental"),
                ("Bratislava", "Castillo frente al Danubio joven", "Continental"),
                ("Budapest", "La perla del Danubio, balnearios y ruinas de bar", "Continental"),
                ("Debrecen", "La Roma calvinista de Hungr├¡a", "Continental"),
                ("Viena", "Capital de la m├║sica cl├ísica e Imperio", "Continental"),
                ("Salzburgo", "Mozart y los paisajes de Sonrisas y L├ígrimas", "Alpino"),
                ("Innsbruck", "Capital de los Alpes dorados", "Alpino"),
                ("Bucarest", "El Par├¡s del Este y el gigantesco palacio", "Continental"),
                ("Cluj-Napoca", "Bosques de Transilvania y capital joven", "Continental"),
                ("Sof├¡a", "C├║pulas ortodoxas bajo la monta├▒a Vitosha", "Continental"),
                ("Belgrado", "Fortaleza frente al encuentro de dos r├¡os", "Continental"),
                ("Zagreb", "Ciudad baja, ciudad alta y techo de colores", "Continental"),
                ("Dubrovnik", "Desembarco y la perla antigua del Adri├ítico", "Mediterr├íneo")
            ],
            "Pa├¡ses N├│rdicos": [
                ("Estocolmo", "La belleza asentada sobre catorce islas", "Fr├¡o"),
                ("Gotemburgo", "Canales, tranv├¡as azules y costa rocosa", "Oce├ínico"),
                ("Malm├Â", "Puente largo hacia Dinamarca y rascacielos curvo", "Oce├ínico"),
                ("Copenhague", "Sirenita m├ígica y parques del Tivoli", "Fresco"),
                ("Aarhus", "Una ciudad de las sonrisas y cultura joven", "Fresco"),
                ("Oslo", "Saltos de esqu├¡ e historia de vikingos", "Fr├¡o"),
                ("Bergen", "La puerta a los bellos fiordos de madera", "Lluvioso"),
                ("Helsinki", "Saunas por todos lados y la plaza blanca", "Fr├¡o"),
                ("Tampere", "La M├ínchester n├│rdica entre los grandes lagos", "Fr├¡o"),
                ("Reikiavik", "Geotermia, auroras boreales y frailecillos", "Fr├¡o")
            ],
            "Otros Europa": [
                ("Lisboa", "Colinas empinadas, fado y tranv├¡as antiguos", "Atl├íntico"),
                ("Oporto", "Bodegas famosas de vino y librer├¡as m├ígicas", "Atl├íntico"),
                ("Bruselas", "Sede europea, atomium, chocolate y gofres", "Templado"),
                ("Brujas", "M├ígicos canales medievales y encajes", "Templado"),
                ("Amberes", "Capital mundial de los diamantes eternos", "Templado"),
                ("Dubl├¡n", "Pubs celtas del Temple Bar y mucha cerveza", "Lluvioso"),
                ("Galway", "Capital cultural irlandesa de los anillos Claddagh", "Lluvioso"),
                ("Cork", "Castillo de Blarney y la piedra de la elocuencia", "Lluvioso")
            ]
        },
        "Norteam├®rica": {
            "Estados Unidos": [
                ("Nueva York", "La inmensa ciudad que nunca duerme", "Variable"),
                ("Los ├üngeles", "Hollywood, estrellas, playa y colinas", "Soleado"),
                ("Chicago", "Arquitectura colosal e historias de blues", "Ventoso"),
                ("Houston", "Tecnolog├¡a espacial y vaqueros texanos", "Caluroso"),
                ("Phoenix", "Calor del desierto y resorts gigantes", "Des├®rtico"),
                ("Filadelfia", "La campana de la libertad y cheesesteaks", "Variable"),
                ("San Antonio", "El ├ülamo de los rebeldes y el paseo fluvial", "Caluroso"),
                ("San Diego", "Clima inmejorable en la frontera soleada", "Soleado"),
                ("Dallas", "JFK, grandes negocios y botas vaqueras", "Continental"),
                ("San Jos├®", "Silicon Valley donde el futuro siempre nace", "Soleado"),
                ("Austin", "Capital mundial de la m├║sica vibrante en vivo", "Caluroso"),
                ("Jacksonville", "Cruces de r├¡os floridanos y arenas atl├ínticas", "H├║medo"),
                ("Fort Worth", "Stockyards enormes de Texas y larga historia", "Caluroso"),
                ("Columbus", "Centro acad├®mico de Ohio y diversidad", "Continental"),
                ("San Francisco", "Golden Gate de niebla, tranv├¡as y altas colinas", "Niebla"),
                ("Charlotte", "NASCAR, reyes bancarios y cultura sure├▒a", "H├║medo"),
                ("Indian├ípolis", "La capital m├íxima del motor de carreras libre", "Continental"),
                ("Seattle", "Aguja Espacial, caf├® infinito y Grunge", "Lluvioso"),
                ("Denver", "La Mile High de cervecera a ras de monta├▒as", "Monta├▒oso"),
                ("Washington D.C.", "Monumentos nacionales imperdibles, la Blanca Casa", "Variable"),
                ("Boston", "La ruta de la libertad intelectual portuaria", "Variable"),
                ("El Paso", "El sol sobre monta├▒as frente al c├ílido pa├¡s de M├®xico", "Des├®rtico"),
                ("Nashville", "Grand Ole Opry y botas de Country y guitarra", "Templado"),
                ("Detroit", "Motor City vibrante y sonidos del sello Motown", "Continental"),
                ("Oklahoma City", "Capital de la energ├¡a con ra├¡ces de Indios reales", "Ventoso"),
                ("Portland", "Ecolog├¡a, raras donas y puentes inmensos de acero", "Lluvioso"),
                ("Las Vegas", "El Strip lleno de ne├│n, suerte y oasis artificial", "Des├®rtico"),
                ("Memphis", "Graceland, el Rock y la profunda tristeza de Elvis", "H├║medo"),
                ("Louisville", "Bates de b├®isbol, el Derby y buen viejo Bourbon", "Templado"),
                ("Baltimore", "Cangrejos azules, puerto interior gigante e historia", "Templado"),
                ("Milwaukee", "Capital del queso frito e incontable buena cerveza", "Continental"),
                ("Albuquerque", "Globos enormes aerost├íticos encima de Breaking Bad", "Des├®rtico"),
                ("Tucson", "Saguaro es cactus gigante de viejo lejano oeste vital", "Des├®rtico"),
                ("Fresno", "Centro enorme agr├¡cola f├®rtil de c├ílida California", "Soleado"),
                ("Sacramento", "Capital cl├ísica antigua dorada del estado del oso", "Soleado"),
                ("Atlanta", "Olimpiadas del 96 y el hogar de CNN original y Coke", "Caluroso"),
                ("Kansas City", "La deliciosa capital del BBQ y docenas de fuentes", "Continental"),
                ("Miami", "Vibra caribe├▒a total de Art Deco y calor", "Tropical"),
                ("Raleigh", "Tri├íngulo de tecnolog├¡a central de gran inteligencia", "H├║medo"),
                ("Omaha", "Historia enorme de pioneros trenes de viejo Oeste", "Continental"),
                ("Oakland", "El lado oriental cultural del puente en la Bah├¡a este", "Soleado"),
                ("Minneapolis", "Los mil lagos del se├▒or de nieves intensas", "Fr├¡o"),
                ("Tulsa", "Art Deco petrolero nativo de grandes r├¡os", "Variable"),
                ("Arlington", "Cementerio militar enorme con pent├ígono gigante", "Variable"),
                ("Nueva Orleans", "El carnaval eterno del jazz vibrante de pantano", "H├║medo"),
                ("Wichita", "El rinc├│n puro centrado de capital aviaci├│n y vacas", "Variable"),
                ("Cleveland", "Hogar rocoso y fuerte del Sal├│n de la Fama", "Continental"),
                ("Tampa", "Golfo verde c├ílido con puros hechos a antigua mano", "Tropical"),
                ("Bakersfield", "Sonido r├║stico crudo vaquero de campos lejanos petroleros", "Variable"),
                ("Aurora", "Amanecer pr├│spero vecino colosal frente a altas Rocosas", "Monta├▒oso"),
                ("Honolulu", "Playa enorme id├¡lica soleada Waikiki y gigantes volcanes aloha", "Tropical")
            ],
            "M├®xico": [
                ("Ciudad de M├®xico", "Mega urbe azteca antigua, museos de Frida y tacos", "Templado"),
                ("Tijuana", "Frontera gigante muy vibrante cruzando al otro sue├▒o", "Des├®rtico"),
                ("Ecatepec", "Vast├¡sima regi├│n urbana conectada por gigante telef├®rico", "Variable"),
                ("Le├│n", "Capital total de piel e infinito calzado global", "Templado"),
                ("Puebla", "Volcanes enormes guardianes y barroco de puro mole dulce", "Templado"),
                ("Ciudad Ju├írez", "Puerta des├®rtica vasta lim├¡trofe norte├▒a cruda", "Des├®rtico"),
                ("Guadalajara", "Tierra grandiosa de puro mariachi, intenso tequila eterno", "Templado"),
                ("Zapopan", "La alt├¡sima Bas├¡lica dorada sagrada muy enorme", "Templado"),
                ("Monterrey", "Sultana industrial gigante cerro imponente la silla alta", "Caluroso"),
                ("Nezahualc├│yotl", "Ciudad densamente valiosa popular gigante e hist├│rica", "Variable"),
                ("Chihuahua", "Pancho Villa revolucionario del vasto seco norte├▒o centro", "Des├®rtico"),
                ("M├®rida", "Esplendor de blanco puro cenotes finos y rica cochinita pibil", "Tropical"),
                ("Canc├║n", "Joyita enorme del caribe y vastos muy enormes resortes turkos", "Tropical"),
                ("Saltillo", "Atenas calurosa de todo el norte gigante con inmensos sarapes", "Des├®rtico"),
                ("Aguascalientes", "Feria festiva de inmenso gigante san marcos nacional genial", "Templado"),
                ("Hermosillo", "El sol inclemente del desierto c├ílido crudo asado norte", "Des├®rtico"),
                ("Mexicali", "El vasto c├ílido sol oriental atrapado de valle c├ílido infernal", "Des├®rtico"),
                ("Culiac├ín", "Capital intensa del vasto y verde valle gigantesco granero norte", "Tropical"),
                ("Quer├®taro", "Colosal Acueducto gigante imperial pr├│spero hermoso central", "Templado"),
                ("Toluca", "El inmenso gigante fr├¡o del chorizar y del vasto gran nevado", "Fresco"),
                ("Morelia", "Acueducto real gigante hermoso centro cantera rosa pura colonial", "Templado"),
                ("Acapulco", "Los alt├¡simos bellos clavadistas cl├ísicos de la bella y grande bah├¡a", "Tropical"),
                ("Reynosa", "Ciudad de industria extensa frontera gigante industrial lejana", "Des├®rtico"),
                ("Torre├│n", "Cristo gigantesco en inmenso hermoso cerro perla gigante lagunera", "Des├®rtico"),
                ("Tlaquepaque", "Arte gigante alfarero dulce en bella cuna gigante art├¡stica pura", "Templado")
            ],
            "Canad├í": [
                ("Toronto", "Rascacielos altos inmensos y torre gigante CN pura en bello lago", "Continental"),
                ("Montreal", "El festival inmenso c├ílido franc├®s en islas enormes gigantes de arte", "Continental"),
                ("Vancouver", "Bosques gigantes inmensos sobre el pac├¡fico infinito lluvia pura natural", "Lluvioso"),
                ("Calgary", "Inmensos vaqueros del crudo crudo gigante estampida petrolera norte", "Fr├¡o"),
                ("Edmonton", "Festival gigante art├¡stico inmenso centro inmenso mall gigante del norte", "Fr├¡o"),
                ("Ottawa", "Canal inmenso gigante bello puente hacia parlamento gigante federal de paz", "Fr├¡o"),
                ("Quebec", "Chateau inmenso Frontenac hermoso basti├│n viejo lindo franc├®s colonial gigante", "Fr├¡o"),
                ("Winnipeg", "Cruce gigante enorme inmenso de extensas fr├¡as bellas y praderas de osos", "Fr├¡o"),
                ("Halifax", "Vasto gigantesco muelle bello mar├¡timo atl├íntico pescador hist├│rico gigante", "Moderado"),
                ("Victoria", "Hermosos inmensos puros jardines gigante t├® cl├ísico c├ílido ingl├®s pac├¡fico", "Templado")
            ]
        },
        "Sudam├®rica": {
            "Brasil": [
                ("S├úo Paulo", "Metr├│polis inmensamente gigante financiera densa de helic├│pteros pura pizzas", "Tropical"),
                ("R├¡o de Janeiro", "Copacabana gigante pan gigante bello de c├ílido hermoso inmenso cristo", "Tropical"),
                ("Brasilia", "Futurismo brillante puro colosal gigante planificado inmenso eje monumental", "C├ílido"),
                ("Salvador", "Capoeira pura m├║sica viva hermosa y el vasto enorme gigante Pelourinho", "Tropical"),
                ("Fortaleza", "Las extensas doradas bellas inmensas dunas puras lindas costeras gigantes", "Tropical"),
                ("Belo Horizonte", "Avenida inmensa Pampulha genial puramente moderna extensa y verde lago", "Tropical"),
                ("Manaos", "El inmenso gigante coraz├│n c├ílido tropical amaz├│nico gran teatro selva puro", "Tropical"),
                ("Curitiba", "Pulm├│n gigantesco verde urbano inmenso parque parque bot├ínico lindo gigante", "Templado"),
                ("Recife", "Puentes puros hermosos inmensos coloniales en el gigante c├ílido inmenso mar", "Tropical"),
                ("Porto Alegre", "Mate amargo inmenso cultura grande pura gaucha gigante bello lago gigante", "Templado")
            ],
            "Argentina": [
                ("Buenos Aires", "Obelisco colosal el tango gigante inmensa boca el bello y enorme puente de la mujer", "Templado"),
                ("C├│rdoba", "La inmensa gigante bella y antigua ca├▒ada jesuita y sierras puras enormes de festival", "Templado"),
                ("Rosario", "Cuna gigante inmensa hermosa bandera nacional y costa esplendor paran├í r├¡o inmenso", "Templado"),
                ("Mendoza", "El inmenso nevado Aconcagua el inmenso dulce vino gigante de puras ricas uvas finas", "Ventoso"),
                ("Tucum├ín", "Casa inmensa cuna grandiosa de la viva pureza de inmensa gigante independencia viva", "Tropical"),
                ("La Plata", "Las enormes puras inmensas lindas diagonales de la bella gran inmensa pura ciudad", "Templado"),
                ("Mar del Plata", "El gigante enorme faro de los grandes intensos lobos grandes de mar y alfajores", "Oce├ínico"),
                ("Salta", "El tren espl├®ndido fabuloso gigante del norte inmenso gigante y cabildos grandes", "Monta├▒oso"),
                ("Santa Fe", "Puente lind├¡simo puro enorme bello gigante colgante intenso alfajor muy artesano", "H├║medo"),
                ("San Juan", "Valles puros gigantesco vino de intenso hermoso inmenso gigante seco viento zonda", "Des├®rtico")
            ],
            "Colombia": [
                ("Bogot├í", "La gran inmensa Monserrate gigante oro puro en el inmenso alto fresqu├¡simo verde", "Templado"),
                ("Medell├¡n", "Metro gigante inmenso cable gigante flores hermos├¡simas pura c├ílida primavera", "Templado"),
                ("Cali", "La gigantesca bell├¡sima capital inmensa salsera ca├▒a alt├¡sima grand├¡sima de azucarera", "Tropical"),
                ("Barranquilla", "Carnaval gigante fabuloso y muy puramente hermoso mar y mucha marimonda muy inmensa", "Tropical"),
                ("Cartagena", "Muy preciosa ciudad inmensa amurallada caribe gigantesco inmenso rom├íntico", "Tropical")
            ],
            "Per├║": [
                ("Lima", "El malec├│n gigante inmenso florido barranco ceviche grand├¡simo esplendor oce├ínico", "Des├®rtico"),
                ("Arequipa", "Volc├ín Misti inmenso pur├¡simo alt├¡simo sillar inmenso blanco de ca├▒├│n inmenso y gigante", "Monta├▒oso"),
                ("Callao", "Fortaleza muy gigante esplendor puerto muy inmenso pura gigante historia de palta muy marina", "Des├®rtico"),
                ("Trujillo", "La grand├¡sima marinera gigante chan chan puramente y gigantesco muy norte├▒o y dulce sol", "Templado"),
                ("Cusco", "El grand├¡simo maravilloso inca gigante pur├¡simo ombligo del mundo monumental alt├¡simo", "Monta├▒oso")
            ],
            "Chile": [
                ("Santiago", "Los Andinisimos gigantes costanera el pur├¡simamente gran alt├¡simo c├│ndor de bella cima", "Templado"),
                ("Puente Alto", "Gran inmensidad de los bell├¡simos pre andinos y los maravillosos de valles lindos sure├▒os", "Templado"),
                ("Valpara├¡so", "Cerros de puro color infinito mil inmensos ascensores puerto inmensamente muy mundial", "Oce├ínico"),
                ("Concepci├│n", "Universidad enorme puro gran campanil gigante rock penquista vibrante pur├¡simo y del sur", "Lluvioso"),
                ("Vi├▒a del Mar", "Reloj gigantesco puro y florido festival infinito monstruoso costero muy balneario gigante", "Mediterr├íneo")
            ],
             "Resto Sudam├®rica": [
                ("Quito", "Mitad pura inmensamente del globo gigante volc├ín del enorme pur├¡simo y colonial y el centro Pichincha", "Monta├▒oso"),
                ("Guayaquil", "Malec├│n largu├¡simo espl├®ndido iguana inmensa pur├¡simo puerto de gigantesco inmenso sol puro marino tropical", "Tropical"),
                ("Caracas", "├üvila inmenso gigante esplendor verde y orqu├¡dea muy gigante puro arepa gran inmensa y pura sabor tropical", "Tropical"),
                ("Maracaibo", "Rel├ímpago de inmenso catatumbo puro puente de gigantesco el lago inmenso inmensamente gran esplendor", "Caluroso"),
                ("La Paz", "Los bell├¡simos alt├¡simos inmensos telef├®ricos en inmensa gigantesca maravilla y gigante illimani pur├¡simo gigante andino", "Fr├¡o"),
                ("Santa Cruz de la Sierra", "Anillos gigantescos puros pr├│speros del enorme gigante vibrante inmens├¡simo gran puro crudo gran tr├│pico inmenso del sur", "Tropical"),
                ("Montevideo", "Las largu├¡simas ramblas costeras el mate espl├®ndido y alt├¡simo puerto enorme inmensamente del rio gran plata enorme gigante", "Templado"),
                ("Asunci├│n", "La preciosa muy gigante madre inmensamente enorme bella y pura guaran├¡ la bella asunci├│n grandiosamente antigua urbe gran", "Caluroso")
            ]
        },
        "Asia": {
            "China": [
                ("Pek├¡n", "Muralla inmensa ciudad pura y prohibida inmens├¡simo drag├│n gran olimpiada gigante y del gran puro gigante oriente inmenso", "Continental"),
                ("Shangh├íi", "Torres alt├¡simas resplandecientes el bund grand├¡simo inmenso y pur├¡simo de r├¡o de vibrante gigantesco el oriente futuro puro", "Tropical"),
                ("Cant├│n", "Cant├│n bell├¡simo inmensamente colosal luz gigante alt├¡simo y centro muy pur├¡simo de feria grande inmensamente del gigante sur inmenso", "Tropical"),
                ("Shenzhen", "F├íbrica gigant├¡sima alt├¡sima metr├│polis gigante futura gran pur├¡simo valle luz puro gigante hardware del mundo entero puro inmenso", "Tropical"),
                ("Chengdu", "Pandas gigantes muy tiernos inmensamente comida picant├¡sima enorme gigante olla y gran puramente gigante y rojo pura bella paz pura panda", "Templado"),
                ("Chongqing", "Colosal maravilla inmensamente alt├¡sima monta├▒osa inmensa pur├¡sima de 3D gigante luz y olla gigante puramente ardiente pura y del centro", "Templado"),
                ("Nank├¡n", "Inmensa capital magna hist├│rica y de inmenso y gigante esplendor puro gigante muy bello hist├│rico pur├¡simo gigante muro pura y de china gigante antigua", "Templado"),
                ("Wuhan", "Grulla amarilla gigante inmens├¡sima vibrante r├¡o yangts├® pur├¡simo con grandes gigantes espl├®ndidos fideos en enorme y pur├¡simo r├¡o milenario inmenso puro cruzado", "Templado"),
                ("Hangzhou", "Lago del inmenso y gigante del oeste muy precioso te pura cuna y gigante alibaba gigante seda precios├¡sima en todo milenario y grand├¡simo e inmenso puro sur", "Templado"),
                ("Tianjin", "La alt├¡sima grandiosa noria del pur├¡simo y del enorme inmenso esplendoroso y gigantesco le├│n grand├¡simo r├¡o mar├¡timo ojo gigante muy pura capital norte", "Continental"),
                ("Xi'an", "Los inmortales gigantescos bell├¡simos muy guerreros y del puro grand├¡simo emperador terracotas milenarios pur├¡simos en ruta de gigante esplendor milenario", "Continental"),
                ("Suzhou", "Venecia pur├¡sima del gigantesco oriente jard├¡n inmensamente hermoso gigante canal lind├¡simo puro gigante y del agua grandiosa dulce milenaria paz gran", "Templado"),
                ("Harbin", "Palacio inmensamente puro y de gigantesqu├¡simo hilo fr├¡o grand├¡simo hielo tigre puro nieve y gigantesca muy bonita y gran ciudad siberiana", "Fr├¡o")
            ],
            "Jap├│n": [
                ("Tokio", "Shibuya inmenso puro ne├│n cruce inmensamente gigante santuarios escondidos puro centro grand├¡simo metr├│polis futuro anime pura", "Templado"),
                ("Osaka", "El vibrante pur├¡simo gran castillo inmenso comida callejera d┼ìtonbori gigante r├¡o pur├¡simo del sabor grandioso del sol", "Templado"),
                ("Kioto", "Oro inmens├¡simo inmenso y bello sinto├¡smo pabellones gran geishas tradici├│n puro milenaria pur├¡simas puertas naranjas milenarias gran de kioto", "Templado"),
                ("Yokohama", "Noria pur├¡sima gigant├¡sima barrio muy puramente puro gran chino costera y frente y a gigantesco bello muy tokio grande puerto y gigante", "Templado"),
                ("Kobe", "Carne inmensamente gigante y pura inmens├¡sima divina pur├¡simo buey grand├¡simo monta├▒a puramente sobre puro gigante mar y gigante puerto muy brillante", "Templado"),
                ("Fukuoka", "El exquisitamente inmenso y gigantesco ram├®n rico yakatai en pura grandios├¡sima y gigante pur├¡sima costa puramente gigante del gigantesco bello y sur lejano", "Templado"),
                ("Sapporo", "Festival gigantesco puro grande de intensa nieve cerviz cerveza gran reloj en puro gigantesco enorme muy de lejana torre inmensamente fr├¡a grand├¡sima nieve blanca norte├▒a pura bella", "Fr├¡o"),
                ("Nagoya", "Castillo inmensamente colosal peces gigantes dorados pura automotor muy industria maravilla y gigante centro pur├¡sima del sol de nagoya y gran aichi", "Templado"),
                ("Hiroshima", "Inmensamente puro y gigante de la sagrada enorme paz de la torii muy gigante rojo gigante sol naciente enorme del gigantesco gran f├®nix milenario y puro gigante del agua", "Templado"),
                ("Nara", "Inmens├¡simo puramente gran gigante bambi buda enorme y pur├¡simo templos gigante sika gigante milenarias pura historia gigantesca parque ancestral", "Templado")
            ],
            "Corea del Sur": [
                ("Se├║l", "N se├║l gigante torre inmens├¡sima y k pop y r├¡o han resplandeciente gigante palacios inmensamente y puros y futurismo pur├¡simo tech", "Templado"),
                ("Busan", "El mar├¡timo y el gigantesco y puro y bello mar playa sur colosal del mar inmensamente pesquero gran puente luminoso de diamante enorme", "Templado"),
                ("Incheon", "El puente gigante aeropuerto ultramoderno y colosal inmensamente gigante puerto pura afluencia occidental de puerta aeroportuaria grand├¡sima de asia", "Templado"),
                ("Daegu", "Monta├▒as inmensamente preciosas de manzanas pur├¡simamente muy gigante de t├® gigantesco sur coreano medicina milenaria en grandioso textil oriental", "Templado"),
                ("Daejeon", "Robot gigantesco pur├¡simo ciencias inmensamente enorme en n├║cleo muy gigante del medio valle puramente brillante innovaci├│n gran cient├¡fica inteligente", "Templado"),
                ("Gwangju", "Bienal gigante puramente de intenso luz en el arte cuna coreana democr├ítica gran colosal pur├¡sima brillante de intenso sol de arte luz y de sur", "Templado")
            ],
            "India": [
                ("Bombay", "La metr├│polis m├íxima gigantesca bollywood inmensa gigante del pur├¡simo majestuoso occidente puerta gigante millonaria grand├¡sima puramente inmensa gran bah├¡a inmensamente colosal dorada pura luz inmensament de sue├▒o gigante", "Tropical"),
                ("Nueva Delhi", "India grandios├¡sima y colosal puerta inmenso pur├¡simamente de gigantesca roja ciudad ca├│tica inmensamente en fort├¡n sagrado loto gigante y pol├¡tica gran inmensamente majestuos├¡simamente brillante e infinita gran antigua maravilla grandiosa", "Caluroso"),
                ("Bangalore", "Gigante inmensa silic├│n puramente el asi├ítico hermoso de inmenso ti pur├¡simo tecnol├│gico silicon grand├¡simo gran valle de gigante innovaci├│n inmensamente colosal gigantesco sol inmenso verde del puro bello y del gran sur", "C├ílido"),
                ("Hyderabad", "Sultanes gigantescos charminar inmensamente colosal del puro perlas diamantes en gigantesco gigante puramente brillante ciudad colosal riqu├¡sima historia majestuosa gran y puro gigante sur musulm├ín", "C├ílido"),
                ("Ahmedabad", "Mahatma grand├¡simo de grand├¡simo y bell├¡simo r├¡o sabarmati gujarati de gigantesqu├¡simo telares puros especias grandiosa inmensamente rica del esplendor oeste del inmenso gran comercio bello", "Des├®rtico"),
                ("Madr├ís (Chennai)", "Playa marina gigantescamente infinita puro gigante templo milenario sur inmensamente puro tamil gigant├¡simo cinematogr├ífico del bello sur con esplendor indio puro inmensamente colosal del mar bengal", "Tropical"),
                ("Calcuta", "Victoria inmensamente colosal grandioso y del pur├¡simo bengala monumento y puente grand├¡simo Howrah gigantesco arte intenso dulce inmens├¡sima bengala brillante enorme oro de intelecto gigantesco pura maravilla grandiosa bella", "Tropical"),
                ("Surat", "El pulidor inmensamente pur├¡simo majestuoso colosal grandioso de preciosos finos gigantescos diamantes gigante colosal puro textil y muy del r├¡o y sur espl├®ndida gigante enorme rica comercial gigante indio sol occidental inmensamente puro bella e inmensa grandeza", "Tropical"),
                ("Jaipur", "Ciudad rosada puramente rosa majestuosa palacios inmensamente gigante inmens├¡simo de bell├¡simos de esplendorosos y vientos rajasthan y de reyes pur├¡simamente resplandeciente en todo de esplendor maharaj├í grandiosa joya inmensa de oro", "Des├®rtico")
            ],
             "Sudeste Asi├ítico": [
                ("Yakarta", "Masiva archipi├®lago grand├¡simo monumento inmenso nacional nasi de gigantesco goreng en capital milenaria del mar inmensa c├ílida java pura inmensa gran megapolis infinita dorada bella pura vibrante luz de fuego puro grande", "Tropical"),
                ("Bangkok", "Esmeralda inmensamente de gran oro puro buda de rey de reyes tuk tuk ca├│tico dorado bello y callejero y sabor pur├¡simo en cielo gran pur├¡simo mar pura y resplandeciente gigantesco esplendor real oro gran brillante de gran pur├¡simo thai", "Tropical"),
                ("Ho Chi Minh City", "Motocicletas puramente gigantescas infinitas del enorme grandioso puro sur phß╗ƒ puramente gigante maravilla gran francesa historia guerra y dragones puro vibrante perla puramente asi├ítica oriental inmenso saig├│n de bello esplendor gigante del vietnamita grandioso pura sur inmensa", "Tropical"),
                ("Han├│i", "Lago de inmensamente gigante tortuga bell├¡sima milenaria comunista de pho pura sopa bah├¡a inmensa drag├│n gigantesca capital de agua gigantesco bello loto norte verde puro maravilla muy brillante de gigante loto y drag├│n rojo grandioso del gran", "Tropical"),
                ("Kuala Lumpur", "Torres gemelas inmensas y de pur├¡simo gigantesco acero brillante de gigante plata en cueva inmensamente pur├¡sima de batu puro isl├ímico futurismo del dorado columpio milenario en dorada maravilla infinita grandosa y gran puro de gran rey asia bella", "Tropical"),
                ("Singapur", "El le├│n inmens├¡simo marino inmenso y verde puerto gigante puro le├│n futurista y muy colosal gigante bah├¡a esplendor s├║per de gigantesco en gran tecnol├│gico jard├¡n puro dorado inmens├¡simo gigante resplandeciente oro sol asia pur├¡simo milagr colosal bella inmensidad del tigre oriental", "Tropical"),
                ("Rang├║n (Yang├│n)", "Shwedagon inmensamente puro y de pagodas doradas diamantes puro gigante puros brit├ínicos colonial templo puro gigante oro esplendor buda de gran oro pura gigantesco m├¡stica milenaria oriental y inmensa bella birmana perla dorada m├ígica inmensa pura", "Tropical"),
                ("Manila", "Intramuros hist├│rica y grand├¡sima inmensa pura heroica bah├¡a puro enorme mall cat├│lico sol de pur├¡simo gigantesco y asi├ítico milenario y jeepney colorido en espl├®ndida archipi├®lago pura luz y perla dorada de bello y grande oriental puramente occidente inmenso", "Tropical")
            ],
            "Oriente Medio": [
                ("Dub├íi", "Rascacielos gigante khalifa de inmensamente oro puro brillante infinito dunas artificial pur├¡sima gigante la y de puro oasis la del mundo de millonario gran bello oro inmensamente gigante oasis sol resplandeciente rica pura perla ├írabe infinita pura maravilla gran rica luz de oriente futurista inmensamente ├írabe", "Des├®rtico"),
                ("Teher├ín", "Milad gigante pur├¡simo inmensa torre alborz espl├®ndida de monta├▒a bello museo inmensamente brillante pura persa maravilla grandiosa en rica capital grandiosa y gran oriental isl├ímica cuna joya de grandiosa de rica inmensamente milenaria pur├¡sima bella m├¡stica espl├®ndida y antigua", "Monta├▒oso"),
                ("Estambul", "Ver Europa en la seccion anterior. Reemplazar.", "Variable"), # Se ignorar├í o repetir├í intencionalmente si es pertinente.
                ("Riad", "El centro grandioso y de reino enorme gigantesco reino inmensa capital de gigantesco oro rascacielos arena pur├¡sima inmensa y del camello majestuoso de inmenso petr├│leo gran puro y gigante oasis sol isl├ímico brillante rico gigantesco futuro oriental grandioso coraz├│n en duna gigante enorme esplendor ├írabe puro sol puro", "Des├®rtico"),
                ("Am├ín", "Ciudad milenaria y blanca pura am├ín romana ciudadela milenaria en pura gigante colinas pur├¡simas en desierto inmensamente puro hache hashimita antiguo de gran de petra oasis nabateo milenario y enorme sol puro del este esplendoroso muy bello pura grandiosa inmensamente historia bella antigua inmensa", "Seco"),
                ("Beirut", "El inmens├¡simo y pur├¡simo par├¡s inmenso grandioso del este del medio inmenso f├®nix pur├¡simo levante gigante bello mediterr├íneo maravilla inmensamente pura cedro verde y pura muy resiliente hermosa gran rica capital dorada hermosa bella perla gigantesca oriental inmensamente de mar milenario dulce y bello", "Mediterr├íneo"),
                ("Jerusal├®n", "Tierra sant├¡sima inmensamente sagrada de c├║pula enorme oro gigante muro pur├¡simo tres y religiones de gigante maravilla divina pura milenaria en sol y enorme grandioso misticismo oriental majestuos├¡sima capital luz milenaria en piedra de oro infinita grandiosa paz bella inmensa luz divina", "Mediterr├íneo"),
                ("Tel Aviv", "Playas inmensamente resplandecientes startup grand├¡sima puro de naci├│n bello innovadora vibrante carmel pura fiesta infinita blanca maravilla gigante ciudad de bauhaus med mediterr├ínea pura luz y del este occidental inmensa perla dorada muy vibrante gran puro oasis sol moderno hermoso inmenso gigante perla", "Mediterr├íneo"),
                ("Abu Dabi", "La enorme y mezquita colosal grandios├¡sima blanca y zayed bella de gran ferrari isla inmensamente resplandeciente gigantesco oro emirat├¡ de millonaria hermosa pura y rica perla de arena oasis de gigante maravilla arquitect├│nica grandiosa ├írabe puro verde golfo gigante de inmensa luz inmensamente grandiosa muy fina pur├¡sima pura capital rica enorme inmensa", "Des├®rtico"),
                ("Doha", "La perla inmensamente pur├¡sima qatar├¡ y alt├¡sima corniche grandiosa bello oasis inmersivo puro oro infinito sol mundiales y bello desierto grand├¡simo golfo moderno espl├®ndido rico columpio majestuoso de infinita isl├ímica riqueza futurista de luz de infinita perla dorada oasis maravilla bella y rica grandeza", "Des├®rtico"),
                ("Bagdad", "Capital grandiosa y cuna de milenaria mesopotamia abas├¡ inmensamente en tigris colosal maravilla y puros d├ítiles antiguo esplendor califa infinito de m├¡stica rica en sol inmensamente gran hist├│rica oriente puro grandeza ├írabe de pur├¡sima infinita y vieja gloria monumental inmensamente milenaria", "Des├®rtico"),
                ("El Cairo", "Ver Africa anterior. Pir├ímides y antiguo nilo en gigante metropolis faraonica", "Des├®rtico")
            ]
        },
        "├üfrica": {
            "├üfrica del Norte": [
                ("El Cairo", "Las inmensas majestuosas y pir├ímides gigantes fara├│nicas y bello enorme nilo de grand├¡sima inmensa khan puro de milenios rica metr├│polis inmensamente bella el gran khalili grandiosa antigua maravilla madre del gigante bello esplendor africano", "Des├®rtico"),
                ("Alejandr├¡a", "Biblioteca bella majestuosa faro espl├®ndido enorme y gigantesca de ptolemaico mediterr├íneo grand├¡simo y muy bello egipto sabio de pur├¡sima costera inmensa maravilla brillante y bella alejandro gran", "Mediterr├íneo"),
                ("Casablanca", "La grandiosa hassan majestuosa inmensamente de puro gigante mezquita segunda pur├¡sima pel├¡cula inmensa marroqu├¡ rom├íntica la gigante blanca atl├íntica rica perla grand├¡sima bella del occidente africano resplandeciente en blanca muy gigante pura paz y rica luz occidental", "Mediterr├íneo"),
                ("Argel", "Blanca y puramente argelina inmensa casbah gigantesca majestuosa fenicia colosal frente en bello al grandioso gigante mediterr├íneo rica sol muy bello oro milenario capital hist├│rica de hermosa bella brillante luz africana pura dorada grandiosa", "Mediterr├íneo"),
                ("T├║nez", "Cartago antigua inmensa gigante medina africana inmensa majestuosa de pur├¡simo jazm├¡n del dulce grandioso mediterr├íneo bello sol historia p├║nica maravilla en el inmenso dulce rinc├│n gran rico occidental dorado norte y bello africano en esplendor andalus├¡ grande infinita oro espl├®ndido pura blanca del gran bello oasis de nor├ífrica", "Mediterr├íneo")
            ],
            "├üfrica Subsahariana": [
                ("Lagos", "Gigantesca inmens├¡sima vibrante bella metr├│polis gigante puro afrobeat en gigantesca grandiosa gran nigeria bella de luz y rascacielos enorme pura bella infinita continente africano gran dorada de la gran gigante inmensa rica estrella del gran ├ífrica occidental rica", "Tropical"),
                ("Kinsasa", "La gigantesca riqu├¡sima enorme grandiosa y vital arteria pura inmensamente en congo bella colosal del ├ífrica profunda grandiosa y de rumba maravilla en bella inmensamente y gigante r├¡o pura espl├®ndida pura metropole de bello infinito muy fuerte sol rica infinita perla del grandioso gigante coraz├│n", "Tropical"),
                ("Luanda", "De portugues├¡sima angole├▒a de inmenso mar del atl├íntico y rico milenario puro grandioso brillante oro en inmensamente del petr├│leo bello en gigante esplendor pura y resplandeciente joyita de oro gigante y africana bella gigante sur tropical de rumba gran dorada viva capital pur├¡sima africana", "Tropical"),
                ("Nairobi", "La gigantesca verde grandiosa bella pur├¡sima capital gigante safari de masai infinita pur├¡sima reserva inmensamente gigante africana inmensa le├│n inmensamente en pura colosal llanura bella perla pura del ecuador brillante de masai sol gigante inmenso del bello centro pura oriental luz de oro infinita", "Templado"),
                ("Ad├¡s Abeba", "La inmensa muy grandiosa y bella flor nueva pura et├¡ope en techo pura grandioso luz del majestuoso inmensa maravilla ├ífrica de sagrado puro inmenso esplendor rico del caf├® cuna majestuoso oro divina gigante bella altura continental infinita pura brillante bella africana oriental pura milenaria enorme joya de rica gran paz dorada", "Templado"),
                ("Dakar", "El extremo muy occidental inmenso y pur├¡simo baobab gigante de goree isla colosal en senegal bella rally dorado grandiosa atl├íntico puro inmensamente faro brillante gran infinita luz africana de pura bella perla oro esplendor senegalesa viva del gran oc├®ano de majestuoso mar", "Tropical"),
                ("Johannesburgo", "La inmensamente pur├¡sima de gigantesco grandioso mandela de oro majestuoso en profunda colosal mina sudafricana pura y gigante soto e inmens├¡sima capital vibrante de riqu├¡sima arco├¡ris oro del sur inmenso brillante sur dorada maravilla infinita de gigante historia negra rica sudafricana de bello oro perla luz puro diamante y gigante sol inmensa de afrika enorme rica viva", "Templado"),
                ("Ciudad del Cabo", "Monta├▒a majestuosa mesa de majestuoso gigante grandiosa verde esperanza de inmenso gigante el buen cabo puro de maravilla atl├íntica de muy africana maravilla en el pur├¡simo gigante inmensamente faro de brillante luz fin del inmenso continente bello de majestuoso y puro esplendor de los oc├®anos inmensa hermosa", "Mediterr├íneo"),
                ("Durban", "Costa dorada pur├¡sima sudafricana colosal brillante zul├║ gigante playa de inmensamente y de indio surfeador inmenso gigante esplendor viva maravilla de pura rica sol enorme gigante dorado inmensamente bella indiano perla", "H├║medo"),
                ("Akkra", "Estrella grandiosa pur├¡sima negra en golfo de dorada gigante maravillosa ghana viva puro imperio costa inmenso del gran hist├│rico occidental oro de brillante luz africana viva esplendorosa", "Tropical")
            ]
        },
        "Ocean├¡a": {
            "Australia": [
                ("S├¡dney", "La grand├¡sima pur├¡sima ├│pera majestuosa con inmensa concha blanca puente enorme brillante gigante de bah├¡a inmenso canguro maravilla puramente de playa bondi en bell├¡simo sol del esplendor surf puro inmensamente pac├¡fico bello y enorme grandioso sol lejano pura luz", "Soleado"),
                ("Melbourne", "El callej├│n grandios├¡simo pur├¡simo victoriano arte inmenso callejero brillante tranv├¡a colosal en pur├¡sima gigante capital grandiosa canguro cultura de bello sur de grandioso y vibrante esplendor caf├® puro gigante luz oce├ínica fina inmensa", "Templado"),
                ("Brisbane", "El sol brillando inmensamente puro dorad├¡simo colosal de koalas puro gigante tropical de bell├¡simo inmensamente colosal y r├¡o queensland gigante y muy puramente capital oriental austral grandiosa bella norte hermosa maravilla vibrante en oro playa pacifica pura infinita", "Subtropical"),
                ("Perth", "La lejana maravilla muy majestuos├¡sima y pur├¡sima brillante gigante oro metr├│polis occidente inmensa bella australiana de bello cisne gigante puro negro mar colosal luz grandiosa en inmenso enorme e infinito pac├¡fico y dorado inmenso gran cielo brillante pura bella de sol puro viva austral", "Mediterr├íneo"),
                ("Adelaida", "Valle inmensamente colosal grandioso y de barossa pur├¡simo canguro bello inmenso y gigante y puro iglesia colosal sure├▒a capital grand├¡sima pac├¡fica dorada inmensa en grandioso vino festival gigante de arte oro brillante", "Mediterr├íneo")
            ],
            "Nueva Zelanda": [
                ("Auckland", "Ciudad gigante inmensamente y pura colosal velero volc├ínica skytower inmenso pur├¡simo en doble puerto kiwi maravilloso en se├▒or grandioso inmenso pac├¡fico sur de los grand├¡simos y anillos majestuosa bella verde maravilla infinita neozelandesa pura de luz hermosa infinita perla grandiosa viva", "Oce├ínico"),
                ("Wellington", "Capital bell├¡sima del pur├¡simo grandioso y gigante viento cable inmenso car puro museo de gigante maor├¡ colosal infinita perla en se├▒or pur├¡simo del grandioso del inmensamente sur de rica plata majestuosa del grandioso pac├¡fico luz brillante viva verde de inmenso sol pura brillante de inmensa orilla majestuosa", "Ventoso"),
                ("Christchurch", "Jard├¡n inmensamente colosal grandioso pur├¡simo majestuoso kiwi de inmenso y resiliente bello puro grandiosos majestuosos ingleses edificios colosales del pac├¡fico brillante infinita del muy inmensa de sur majestuosa luz pura verde maravilla y bella lejana viva perla", "Oce├ínico")
            ]
        }
    }
    
    TIPO_EVENTO = ['M├║sica', 'Deporte', 'Teatro', 'Arte', 'Gastronom├¡a', 'Tecnolog├¡a', 'Festivales', 'Cultura']
    
    destinos = []
    eventos = []
    
    id_destino = 1
    id_evento = 1
    
    # 2. Generar todo
    for region, paises in lugares.items():
        for pais, lista_ciudades in paises.items():
            for c in lista_ciudades:
                city = c[0]
                desc = c[1]
                clima = c[2]
                destinos.append((id_destino, city, desc, clima, pais, region))
                
                # Para cada destino, generar de 2 a 4 eventos
                num_evt = random.randint(2, 4)
                for _ in range(num_evt):
                    tipo = random.choice(TIPO_EVENTO)
                    name = f"Evento de {tipo} en {city}"
                    
                    if tipo == 'M├║sica': precio = f"{random.randint(20, 150)}Ôé¼"
                    elif tipo == 'Deporte': precio = f"{random.randint(15, 200)}Ôé¼"
                    elif tipo == 'Teatro': precio = f"{random.randint(10, 80)}Ôé¼"
                    elif tipo == 'Gastronom├¡a': precio = f"{random.randint(30, 100)}Ôé¼"
                    elif tipo == 'Festivales': precio = "Gratis" if random.random() < 0.3 else f"{random.randint(10, 50)}Ôé¼"
                    else: precio = f"{random.randint(5, 50)}Ôé¼"
                    
                    eventos.append((id_evento, id_destino, name, tipo, precio))
                    id_evento += 1
                
                id_destino += 1

    return destinos, eventos

d, e = generar_datos_masivos()

print(f"DESTINOS_POOL_SIZE = {len(d)}")

content = "DESTINOS_POOL = [\n"
for dest in d:
    # city, desc, clima, pais, region
    content += f"    ('{dest[1]}', '{dest[2]}', '{dest[3]}', '{dest[4]}', '{dest[5]}'),\n"
content += "]\n\n"

content += "CITY_EVENTS_MASIVOS = [\n"
for evt in e:
    # destino_id -> we can't use id because setup_database generates its own id.
    # so we map to the city name in Python. Or we just keep them separate and inject in setup_database.
    pass

with open('datos_generados.py', 'w', encoding='utf-8') as f:
    f.write(content)
