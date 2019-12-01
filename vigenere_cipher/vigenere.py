# Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().

# print(chr(97)) == "b"
# print(chr(98)) == "b"

# print(ord("a")) == 97
# print(ord("b")) == 98

class Vigenere:

    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        cipher = ''
        i = 0
        for character in message:
            unicode_code_point_of_character_minus_ninetyseven = ord(character.lower()) - 97
            x = ord(self.key[i % len(self.key)].lower()) - 97
            cipher = cipher + chr(((unicode_code_point_of_character_minus_ninetyseven + x) % 26) + 97)
            i += 1
        return(cipher)

    def decrypt(self, cipher):
        message = ''
        i = 0
        for character in cipher:
            unicode_code_point_of_character_minus_ninetyseven = ord(character.lower()) - 97
            x = ord(self.key[i % len(self.key)].lower()) - 97
            message = message + chr(((unicode_code_point_of_character_minus_ninetyseven - x) % 26) + 97)
            i += 1
        return(message)

cipher = "yuebvhprzhhniiqcifzhfcorllfwfopatutgfhegiydrcssyzfmcisjljujbkipdgippwomjsyqmjngytytllajlklpblwfbzgqplxfltytcvmbwlhqjvutgeaecmioqycscrwdcgnbltytmeyyckysjfhhciqjquinersomixfqzaoyxybknybryysrfyorvlfbeisjrhelfcoqyixgeatcipjavhppiyqcrnfbjjfybcoejbzygjfrznfcowjrvxjryutrzfzyejbqkoscznpzjystvmosxbblubpuuuscyysckipsejmcrmblkhppucngeougfhfvtymjvhdcrjbpkgflkmjkglvbvhdckbfkvnocnxsynjbpknicdbfyenpfvlpmwiojpgvqzwmcrpfqrsemfltfzgumiycpvxgmigjdjchftutcrmemjnbwzhhfvhpjfilgeajduipnzhjmemflkcncentursvluysqkipbvhenrlugrfjrpuobyctklmuwfoxgkbigdzsmdbjkyysuvlfkflfgeymbvmuzvcupvmvjkmimlfepvgbpbpblznzqhobpvooncybqrhucjjfazumjputqzmuyewfqlzggtcflkbfafgqyictmempgekvgvnvbvvsyewimeytfpyeurleqkujpjnvpeyefrmmynqpluysffltcjxftfhtfzlfgepjrrnjmexjqtiwciyemlnjluomevhdckbfcowfjcyoavjscwyscewfmsdfakcplvmugducjvxjqtivpjyqpfwvpzhhfvbfpvgbgecoefhegjnssjntqzgqjzwjrpugdiiorzhhgekvgvnvbvzppeixqpgqykbjxvuhcjbfkvuoreyxryyjpjyyafombuygciwigcxblcitcrnrsznumccgcuiescfemgfbwkbfwdctqxcwcjivnnisbjnpsgmuwcypdjcoavqppcxxccybdkitllapleiocvxxypixllhdmdgplcsuprpfjccoeeixytwfnkuoavvfbtinnccncentmccdgkoecuctqzgjjrlbbdcsykcpljiucigjlrnfbeijltioriutrvxjrrxwyenbevmflklfykcfqdlicrjbpkgflkmemccngkmgyisfrkoslvxigxbmwiyqyzlqyictfkumivxtgoxsynzplulblbzppdhppkbfbrsfyklfnlftgmyrsvmugfhtafhucenfbycndvqfvkyoqzpfqljqminfbfzscdusirvmwkbppfohfcsicrjqcrlbltyjljoqnfmjlxnpjvlbzcsbngfbsuyemiigzvmvdwysgeavlwyfjzhhqfichvwugfhbeiyfysffycfpurhdcdypdrmluznigeyorzlfqvutmemfvtinkfhgyiqimwungcsbqsywycffwnuskkbbqjoscfhqyiehgifufvssgtbimllocnqfjcqbwpivdrwfwvvfkvvfcelpmdqfqfhtdfheyewpsenswuyncjhfkvmtyxyjrsudfvfppuincjnjavrucexfbuivzkzvjrmdmewfpembrdislzhhnioecenscdiwycuojvnucimcwfhdmlfekpcomixfpeywcicumiyyaznfbtysrrcoqzrucvhjrkiqyinjcjwpjfhfjuyqcexjlxwplmyzgeaegiydrziofrmmcucnkvxjykymynabrvbfpnymjsyejzzfdvyuqvyopvhumehbrllfmihpcowfnkcuqlmtcouekzlbrzioqkcnscuucuwvjkcwykyepvutmeucjvvfniikctnjmejpqjytqziomwlfychplvuspfinwvvscumbivcgqfgfgjusprhhgeagsihjqyyeieixjvxhcrascvucjvmpdrhowrmtkzffsgmnycfjrmomerldfrnuwjcnncynmeniqkoslvxpfrndfrhhcfzbqkiogjbfbjyucojscjmjmempjzwjrlxfursbbdcsykcplxlfykfzfvusrvxiyjqimsymgvpfbicgrrfmmnascvhtmeqbjcmzcrltdflcjlmiqzlnyiabpvneprqjlxmscgybrvxsctospvxfvvldgjymylaigeanypspssoubflfnvuucuqiykywcinpuvfdmdyeysmpjlnflfzbrjosnictcrfuffohffoujzpfbrhegezppdyeqysegjmvyuyqpfjfpksnsjcdycvzkvnipfohfyyeprqjlxmbtzhhqrhomnytrrheymijbuydypbfyixnptinkfhtmncdivnbngybpkitsuxflnisryspljbbbvigmwzfppyxffffqkipbyiqcumimkqiykucjvwpjuhfukbfqvyimcxgpzyobcsbqrhccklbwvxgmigfpcsicdislzhhzvwbsjybqkitmtcfrpvffrpfbdincentnlnmyucfquytgxhnpjmjqkysurmqjrsplycmjwymraiileihykybkgutqvxggxosckinyiefbzhqpfmqciivqdcebcyumemjqpyjlyucgkcoermbqjctrrhdcdyfqgydgrfmwwisjfilgeauufwpsjcoqiyhscusydioejnxyjwfpkujlksscdujlzhhceasmjmfbrjqjroecumjpyixbzmdmmyswjyurcyemgcogfhimnyohfsfbxlfykyshfsbbrjucunpmjbzlfqqpfjfpcstsijsgjyfvgyoqvmjlkyscjnomilfncsjlxmicjbfzflfrrfmlrsnyesnyesugdyzckffqjxpssngsczpprhtuvlfbfhfdrnjluomevxnyiabpvntgimisknfpjnpevnicifbbzytqfcouyimjpusmlheuyyoavcoykqbpdnifvoqezpjlxiqnfmfgwcnnfmtgsffgjxjqjcngcuscenscrnjcjiimenfpdcoykyecrlocjntrlxjcuusrzwmctivlklzrvhscjjfakmimncoeyuezlnschojpvxpdwysgeaigdymcxuoavmplzgqpfpfbzhgmigfbjuwgeatfvlqjvutcuuscjywciumqkusrvxgcdumcjgfrjbppkbfpeiuydioesyjlxuowkbjlxighlxhcwlvgkwiyigwgvqtbfgjjvmnprhgminzycioermicjbfcuodykcplxyukzxejvnpluuzyxlfcdyorgysdflncujscjystvxvlncmjzhhbfbpuvpfprmqjvutcuigdvhdcfouurlezvfptvxcwglfqvhuzpivrnusbeyjryysfvmpafpfpvxbkzucjvascrnfpaowcecmcglpnfmbjsyuprsfbyyblzhgmigfbnyebzhhqwimjfqfbglfarougfheypmfczgqplxfltytwdjbrycacgljltcqjvmbrwomjcybdxcwchojrkijlkbfwljplvuetrhdcuxjtvlucuxpkvmugtmfviyqcrnfbsljlxcoepivmcxqmjmjzcyqpfwvpvxicinsgwfjlxfbsxbucinimlairjjsmgysrpmicdyuursdmdjblzioqjbzfrxtmccdgkoecwuwmllbzcypueqigtbdmlfeqrqhsvmukrhomnbfyixcskfbqkyekpwpkzhhseybqpgbpbyeqfmimlfeeiuwgksmcknfpjcuydioejnicimfjwxfyiytrrhxgexpujvzufiecufbbzytqyycyjefrjybqfhbevbfplhfyjstynxjqtivpjyvlncmjzhhydhpbvmdpzvfbuykctnjmecoafgnmuyomcctrvhjlxigzvzppvhbrllffzmqyictfsizyewpsenswuyncjhfkvmtyxyjrsudfvfppuincjnjavrucexfbuivzkzvjrmdmewfpembrdislzhhnioecenscdiwycuojvnucimcwfhdmlfekpcomixfpeywcicumiyyaznfbtysrrcoqzrucvhjrkiqyinjcjwpjfhfjuyqcexjlxwplmyzgeaegiydrziofrmmcucnkvxjykymynabrvbfpnymjsyejzzfdvyuqvyopvhumehbrllfmihpcowfnkcuqlmtcohpbvjflucoesydmepjltyegeoodvymgeaicvrdccffltytfvooywzfakyeyexumfmflkcncentfvlsmfgtfvxpmimufvlfwvuxyiyjlsstfrfmcuodykcpliynyzhecicoqfwppucbjcsigjlfkrcobvlbluixluykctnjmexbsxbucimtnfluqdyogjybqpnpmbbfqyyerfejluzpjcsxyjnicjyufiyfyextmeatyiitcnbpqviggepjazhjrpwplkynnknpevniciconfmtgsffziuoayyeyjmvpvxdmdjblpbbqkcmwcipizhherlsckmjlfbnmjniymymmmynwxiockiufzmtmuctafpfpvxjlkyscjnfbglpqgysmlmufvivprzgpfhugeajljcqgucuwuuzkzmtcufptvltursplvpblznzuzmicjhbwsousjytfpmfcdyeuznigenxcenzuzmicuimbwyxpvasckjbqjyeysmpjlnfmeyiyjnflvxnpjuowjyoqzvmcrhtgewfpznzqfyyriyngksicrxegkcpljbfppyuryyscklvrygfpznnpjumjglphvwugeagymivprvmceixsejmcrmjlxmplcuxerlecewiyknzrvgqciiiaycmbiyoniiwguyerfgsccyhyewfkrlsgrafqklplxfzmwzdyeuekzlbrzioniitnvlpsjhpuuywmemigiyegdcoskcplcuxdzhjqyyefvlbpvcuqyiomllfbulbuzhhqeisniyurpmfcdousrfufiixlrfmlfnfbnusbkyonrlugtomyiuozfctrvlpsjoqfvlfyjioysfzdiyrsvhujpmftvlbjrhzfrxflaizcumicncoejnvbzyernivnzhucenjmelfkrcobvltnfluqdyozvbbtzivppyiygjjlvmtdvqbercoyesbjfhfqksmcrxecuucmuybqbhbwglphvwugeavlgffyjcoesijqkysmlmfykxjqtiwciyeqffjaznvbvixljcykfgflkmqpfxvavymbvlmwgutrllfdrlbpicwycbpjuivppybpkbfwkyosgioevhujvgbltiorrcocumpgenflkcpljqfckhfqjcomelfqffwgeajqyytrrsjlxuspzpbjrxepvmtcrlocjnumglfdvlfltydmemjbvlfbznufvgtccpfqzhrszyusuydmcffakcoevmugduugeawgvqqyiegmiqiwxuzieyxdrwflvruryuolvusrfzpsimpfrherzgfqjiemyyemnhtkvqpscxxgknzysiecgusrpbfpwivlukvgvnmynnicpxpmizpsivfbwujjeixfrpfgemjnzxjrpnicjogdzwjcenegjwsckcplzgqplxfltyscjimskcpljcsfzgectctgmymwglpavyeffqblpyoerafbmctgkiscojmyzhfbglpnicfrpigdfounvlqckobjyctwfogcvftmcxpdwzfjkhbwiitcdyuwfoxcjiflklfykcfqtomrzpbrvxbqkiogjbfbzmxyjmjqkysdflgcnfplxyskimtsuxflkumcencctincuiocduzzflfolcucmcmmcxngcyjdcclccsbkfzccrouwkutrvmqpfdfakcoejospfoobvxmgkysykoscpyubvfjeyngscumrvlbrziozlnccugflfjflrlfdiinjfhhuysdmcxjddotrjhvessvnfhtyeammlxmcwnbqdyemglfdvlfltyflklfykcfqtinnccncennmkcplcytqpymgkysykoscuuzzvbbtzivpvrqjrcocufbuiynyzhecijsmuodctuoafotgembativlkspsgutrllfnvwvjzusbvfjarnfyejmcrmblkjsmmcecuxpnvldczpffvlfvkyoqzpfnvldczpfbduzyestgewfpznzconscdcuwzhecvxbbulbryyskrsqpvnuwjyfmcxqpfjsgvnzbvfjeynfbvrqjrcocujfptyjtvxpryysuzmfmsdfakcpljuxrvhicixpssnncicuqzlufvljeynufvmfyciocbyfnjvzqfgfrzgfqzhucenjmemnycfocjmiceisryqbpuwpljctrvxxcfniciqjqvusprhhgeadmdgbluyebzmdmmyswznfvgfbgeyebfytaffecmyoqfhhjzefrnizckvfcefjrvlbrllfgenfpvmucuuolfooazhhdflucigjlrnfbycngekvgvnvbvxbwjbzfzgtcczicwysrzffaycdivhqcibbnjqbgkcoezzigxbfqkhpgkwplkcosvxqpfgprziofrmdmemvjkyedrnjkglptzhhlfnxypcuniyqyiyjqpyomkbjlxvmsjbfqljcpfohfkisyjasymcuwgutrllfjzgjrvxftvhjlxiouzwlckusmlhezvuvrpmbwjbfdiuoieytqiytcdvmcumbweiulvqtkrfmlvmtwfoegjwptvlzlfctgvlgcilbpjsfrjbzlvmtuvuufvlucewpjfhfjkipfzgigdmfjwyoerafbyotzrhenlltsznnsjcdycgblrafzlnigdxfrvlngeydmemjqkyeryyscwiscucolvlumsyzmexscxlfrnctfvxblslbltbiciynyzhccuvvrvrqctntswzfpccurcyscgujpwomdzfmcuxjpvwugfhvqvwplkcosrftckbjkglpnicfrpwplkcosvxtyngfrrjqjroecuzbtfosgkyecwcdgvhuceasmjmfbtioavumcuuobyysafhdjlxfbsiznvlqckobjffeqljqmjcoewusryyspvfbrvxccuuobgutqrafafggmindgmcmjpxbqyqpmumtcvzsyeeocjmpzaydrzioyscmgkcfqkbfyjbbqkyocuiiniiestyeniitnvwudflncifzsgunncudgeagmigjlxhbwcipizhhmcxnyiljcuzfuyutkrlhyiyubzmqmjyeyuxtaiyflvxscexfpvxtgombwyctqkljizhhafhggeyernifvhojqznfmsdfakcpluymgxbucuxfdzwjcenzckcuqtiorrcocuwppucbjsydylmfyiybativlkywguyorzntqlvkctncskybrtuoniiqcifzdffmmnyejvuslzhhniyqyiyewfoemlvudlfzckbjkfpfpduowfosefiejrxzdvyuyjeufrnfvgyoqvmpuegpbvlbrvxbwwuuricgjzhhqklplxysqzlemdytrzwgcvfjlxmjrjymdrnccrhtuvlbjnuzqvrfrvlvnuiuffohfflnwgfflksvlvutwuigpzyobjbjnjidmemjbvlfbiynyiebzcscckitcenjkvhuqfzgciyekvhugfhhpvuucizjdkyflfhfniingjycctuvqvhppnbzbvhprzhhqgybizhhdrnjluomevxtynxxccfjlxlbgcffppbfyjwpkgfjkvhuselfqvlwcujsmaydrzhhzvnxcvhiyuicqvlwcglfrvhebvfjeyngmivfjzywcuiocnmqygysolytrzioqtioqlfucumxcvnocjmemfosqgisrjgblyctseqjjccoewomdzfmcuxfnrlusiymynhpunisjuixlkiuycmbtvxbzfpffvldylmfrrvmcncdivnnwjymdyysqhobpvlfkrllryytffombwusqvwvpvmfvjgjjzhhafotgemxyilblkfbuvrqjrcodflxfvniciungwhvksyslfoqnvljmulferleqlxecevfrkysbvwjqzpfjpmvpiivluyeycfbbdcsykcplrhelfnzmlivrgusrzwvjrltwdjbrycaceiudrppsiucjvcoriiestyegemjnzxjrpvvryunprnicihvksysarhblumfrglbgjyegjnssjntyecuafhucenfbgysavcwcuuurvhegeapfkbppfohfcsfqkcnykcoezhupfxvavxtrzgvjrnfbnbzzlnnmkcplcytqjcusrnjmeuekznugeaqpfgprzioykisrfjfptyjtvxccdlbalnflvmtuvutcjnjkrvmcvhkmpgflkoqyebfjufbrvutdvfuieixjvusluibjcixqffjbkihprpfkzxejvnpljotnzwjmeuhcyysyknflkcpltbjcwfzqvpfprfccucuqnctfzhhgjmpkfgflkmpltbbksysniytqvxumuivzkzvjpyuursqpfjfpcsbljqfpvxisduogksjrjxfqzlpsjgjllnfpsymgvpfqvlwgtybpicwcuwjtzfmwrxeycfbalnflvmtycfpurhdcrhbrvuhcihfqjzbtfosgkyjlvrucemjtvyyolctgkyzcrgggectfvxscaijavxeprqjlxmtmyyfjvabltytckfpqvxfyioqmebbbkqpgkmxfrntcvhiccxtfvmjpyixieixuyuuqlwiuyincjnfcdjvrlhfyjstckjjolyeqfhecgyobyysmkbfpjnxmuybpyymbdltdvyutzyxfvlpjuzjlvvppvwblcyeryuoffqiyjlblbxjqtiwcisblpyyrvhtgmyiyjwpkduobvxegiydrzioqyisrrngpfhuuycdfsfjluutwvutniidsicoelhxgcfjlxjsgewjncycwrhdmlhuppxfkvmocdytqrafgkvbayymmixpkvmugtyyrvhecuxpssngscutafhdcihtykgppecoeglvbvhupvgptrfblcyurvltzpioafombdsjlflecihftvljrflfvtcucuwfpkujljcyrvyogknpnrlugvmdmcioccxfnvhegeadmepfwzhhbzlfakcplyutjvxjkdyegrnfjrqhykyiciqfjcvfbccgcwyfrjyfliyorfhoykoscflomvrdcgnjrjotqvrscdujlmumjvsxffgsqlhfyjsscdiwcnipbvxigdspsyysolytrzioqwuwmlljrvbjktioavumcuqfrfqjdvzbavnpmbbfryyuyjnfzvajlvusjpimbnbzqzhdculjcuwblwcsqkjscguscuutmibvkfoscuzppdysjpywgcgsqklvcxyunfmucojscjmwgcfbevywcecoeglvbvhukputwvbvlulfbwiskzhhryiveyntqyyxfphprucsctnmwiytcipfbgudirafqpivuzhuciuoqzfflkzbtfosmwunrvhecugvrlumlflicewfffjfbyysywnfpfnicieomnhecwysfzmgmiwpsenzlfqtgjnfpvhhyxyiyumfyjiozvnucibbbnujrvxpatutgfhbjdltgenfpvmucuzbpvrqpvmtgfhbatyqrrhdcuuzcznicigsqkumcenqscffbdyoprnicilfeiyuyugjpvvvrccgcpytybyjrjbfbwcwccuewyydmcxjldyfrljtcipjavafrdyuyuuqrvxnyknfpjigdvhdcwisnicoazjmcjgblrhzgemjnzxjrpuhcpivqzgqjzwjrpoobvltrfiebfigdvljlxjmcrmvpvhpctmuykcduyuucmysmegsbzlfakfzryitcrhfolumnfcoreizcrltbfxfnvheurlnryzbrsoufvlcskjmypyeqysblumvzaydrjqpluyscunsgwfjlxjmcrmblkjssuyortisbzumafggminemeipltimmeymyjutqllfbtbjabyoqdusrdltbrsxfzwizvajljhveuitmcxnpznjdjodfkyskzhbrvxvltinkfhmwrnbrvmugduugeanyevffrpjmllnckgpmefjeynfvklfkznzytouceytqucsctnjmebfmgjpqvuurylpuexfqzlfmwhpyehpsewjlxcnniytqzioseugdvwucuxbwyctyiyvliytcipfbzhescafltyigdbbpuzjlulfyuuscpivqrhhnrlmmimwgjcucuhpgjcfpyixcojmyzhqjvutcubjqjyfqljqmjyemrmiydyeyjmvpvxpliymykyemwzfltybrvkvycfzrfnbjcsvqvgjjvbfpnbpkkbfwzntivjufffeyeqblkutfvvscuigurmeyjbxmfxmyexmmixdfvysdlfisjvblumuufytrrnfuysufvcsqzhecvxigdjpjznfmcxtcknmckbpsxbtfvcoyjuupvabpuybqzfzlrlsmnlpsjyeyucfsjfvabcmwwljcextbfutfrgfbkiemjoqnfmfricfbdyblkgsqdcmcjifvhojqznfzvbbtzivprmumdcebcyumejfpwydrcsdfzwlcehpuzmigeaxyznjlxunqrsdmewfpemeuvfmgeahprwfdlftgobvkfoscuqickbfpdlvnjuwgeatrrflgeablrwugmynskobjeisdrnicigpryyscoyuciwiyeafqzreguumjzaomiuorjuxfvlicixsyncoejgbpicbevfbsxbuciwbqviiyeniykisynuzqzaibfbfpvoqmeudskyocjmzmlyyolctgkypsimfjmytlfqfluzppwyjrvxflhojpvsfuznimlnjrxuspvntsgbjkjymdzhuciytrfoslflsctyjtvxgmcfpuvxxyjwvjkcwykyeyeoqqffjaznvbvgssejmcrmblkbjqvrrszmjrvmjltysgksfblwbrzioqyunccytqkyocrlocjnmwslfybzbqkuebjixcdyvlbhpueutgdjsmmyiyjnjjpmjrkcoewiskzhhcjjfazumjpzbtfosysffafgqjzgflkvvrkbppfohfcsvliytcipfbjuxqyyufvgtccpfqjogdzwjcenjkgitqzvmcycnkrsucecoqvhtgsffnlndmenjllcoefjqmjyfvvnfpzhdmdytgdjmcwyxhfsdmlmjlsournyorpmdycyccxuoolcfrljtffluuiioezhjljjppkmncemiwwisdvcucuyoeiitqvxnypwblrgggectfvxscaijavxeprqjlxmtmyyfjvabltytckfpqvxfyioqmebbbkqpgkmxfrntcvhiccxtfvmjpyixieixuyuuqlwiuyincjnfcdjvrlhfyjstckjjolyeqfhecgyobyysmkbfpjnxmuybpyymbdltdvyutzyxfvlpjuzjlvvppvwblcyeryuoffqiyjlblbxjqtiwcisblpyyrvhtgmyiyjwpkduobvxegiydrzioqyisrrngpfhuuycdfsfjluutwvutniidsicoelhxgcfjlxjsgewjncycwuyqyinemsytmyyflfohfkumcentmtcbzcygmigfpcstgovvryuobjincljemmcfukcnckbfwjbpryydmewmsuyebzmqmjcoeglptzmjmevzolytrzioqrmtgkobrziogkmfqkcnykcoerlfkfnjmeffqjxbwjyorzgflkmfluwbjccoerhjkrajlvuudflcyuybreunceiblnbbrcclcjjprglfqjyekpvzbfugdzrfbyytrlxjcugvayxjbyuearfmlvqepvqufrnlcgnmgdcuqvrqctnxmexfpcuxqyyomnbbqpivtzyxqninyehpgjsnykwikfhfwiipkjnpsglfkrllgkymbvmujvhhryiinrmtcuigdsydylmfwvnngjnbivzfcccoeyutkvhdmemvjkyebzmqmjcoekinmfhmgxbuwvyyriyngksflxuhcgcrsvxjlfhdmdcoervjjznjcjzppwyjrvxtgkobrzioconscdymwdsumyyscjynzcyemcxiyuwplmcdrziobzmdpvnjmeoobvltrfienlnqpzhdggffqpivkrndfdybljefcgmsmlhemeyicikvgtetfvzppdcoekqpafggminjlmcucusfrjbfgewpkvygdvwucuqbpuyorzlfbvmjpvqbwuytgxhgcngsqjyorzgflkmmcumpjzwjrlxfcjnjkrnjlxzsgvheqycqdrnncrhuryitcvpflkctuvylqjnbrvcurfiszfscskbbqwimjpwiyigufvlfgkmjrjzbaknfljjprulfurmdmcffakyebvzjazyorfvkctnjmevzgkxjqtiwcistgewfpznzalljmjcuwhojckxfarsxfflpsexufiyfuflmbnbpjvbbqdltkrhcszfuryydfzhbryysckljcudpivmxfzwiersxfputqllfgeuegvotuzwlckcugjvvrjjpivlpsexqmzhuyexplvdpwfzgcexjlxbfpdiplcchfkgfljqfckhfqjmfclhxgcfjlxigrvhpdznucrltuyimcfbcycftqyuscrhbdwlplkcoezgqplxfltyemyyicvpfppnigeatcofbqkyebzhociqblkyegexfcuqjqyyemlnmynzbprxwyewfbjyurccoejuzdzhjqyyeprcmjvlzmwzfpvxdfzygjpzbpkbfpfznweidmcioccmiweytqjodffhiccjzcjincuippzzjlcuveynfpglpnfmbjcuveycoerhzqfhmynwpljcecihfcuyecowfnkoqnzkvcuuocrnjkrajlvspstbjcwfzdvqfluzfpiusqtinnrmtzvpjqznppwynycytydzfpiusqzhrszlzjrnucifbuiynyieuuffjtvfzrylpuemqmkmfrkbfwbhpuiytrzntprjusiytjrqegmysrvxccccftvxkcehjlxmdmemjbvldfzfepvhufvmfcyuegepjrvxccciwcuwbpicfbkbfaffplvfpatutgfhbjgljltcqjvmegjwsckcplznbqyyvlgffyjcoesijqkysmlmtfvvfbjcoeuybpeixqfhiyczecgusrllfqfuurvhugfhqpfhpsewfqrnjqwcfbuuveynfpjunzlntfpnfbzivqglfqjyeqkoegvxpnzhjmeyorvlfbncobfqtmwzbbmuorrafbvjfluyorjotnzwjmewplmcoavxqpfpjqziofzgzcknjkvxcycftkrndfrncwiipkjqfdrnomkvpweybrcygryueuzninrmufvlfarfmafosreuzkvljrwyxlflqyinzjvuslnbzmllzcrliciyzcjeomnywcebpudljkdyegrnfpvgbgecoetiotvsjlxumjfqbltyemflecklbaksfruymgxbuuicurvhgyinicibjqxyociumgwcoqfvscuuubrlfpfmfjfmfefiedvymyexnybyuuflfycgjqjotcvutwtymcslbrvxeccchfkzvjrhfqgydgrfmwzhdpvutgeajljnssdyorrgjluomevhdctioriutrvxtswzjazyorkivlgffyjuorzhjlzhtcemjzcygymivprvmccuurvlscdusiyoorvxflfohfmomerltypgbljcurzhhfvusrvxplznxgkbpskgfseybqpvbpkioqvyjlxlfkrllfrjqcebjqyutydjpqjccjvigdvljlxuuafhucdjukixjqkuoavmupfhhciuoyknbaygflkyyavfmcewfyehpsewjlxispvutmeucjvunmecggexvjxyoavyyckysrrflcucoyxlfcumqgiculfbfseucjvxpzvnsypyeqyourvltgepjazhjrpcusejbabyegecoqfcnnfmtgsffygjfyiuoavwpljceciyekigsqycnjvzudzheyiyhmfxbqrvtmcouczmcwrgpsenfbiyqcrnfbvhugiymwpysckoslvxufvmfpvuewkcncuyohfsngxbuqzlzckiocjcoavsfyimepzzulvpfpzzdmlfedfluwsyjlxhpmeytrzgbzcyecgyobvhuyjmvdwysgeapldssyeejrcioeyuwcjosczhsmfgxfrnbqyyqmjmfqjcplklbtvfmgeatswzjazyorpyumlluycefbmuogksmmfefbzhumxuznvldczpfjvxccccftvxfluybtflsygnvpfotlfigcjnjkrvmcfbufvlfdflfbzlfakcplljtmemufvywcihprwcoccclcvsfqrfmqllfdvyucmcmrfbpjufplxbfmgyoieyxyehpygusrdyorjidarmjmeumzfctrvlpsjutqffjaznvbvnpgensmuodcuisdzzucvhdmmyscuqfcedpwvxecdytlvctgejscgusczhtrzgvjrnfbdsftvlzrycoeznmgkysykoscxlfykfzcojmyzhbrkynnkjfpyuqqzhgcvfjlxbfffotcdyorrmucsyelfneprqohfsufiiveyyoolcscyixcmysbfyrsrfmwyysqvfgykascrnmwnuzmcxnypspsglfqvhugdjsmmyxgjbjlxnicwyfjzhhtzfmyxyigdgvqzwbjtysrrcojpymqvqiciynwuibjcixyewfyknicrxepvmtdrlufvltgobfyinfbyoobiyerfqbpumisjvbluuscjydsicoefzgmtwbqziopvgfksysbrohfkyspvjmwzhhfvferyuudvymfzmtcvixlpyuqklblxysqpyumyytmdyugdytniiqpzyuwzhtfvljeynqjrnfqvpflyutzvxxffjfptyjtvdvbxgflkxjbdusgrhockcmcumbwuydypmqmzfomnqbjcmncrhuffotcdsnpzhuciytrkbpsxbuqjwscvhfbfzpskqfgxbscdiwgeaftvhjlxmpazyuwdotgtumzvmjbvmjlyucgksfkpfpqvbjjcqfjcoquzfmfviwciiogewscrmjlxmvdwcdgvhucmyswkbjlxgflycnyugjprnjmeooncybqzhhqvrbpfoobiybjcsigjotclhfyjsmmeafpycnkrhigjivpgomjvxoykoscvfjlfluycefbeixdflfvtotciytscnbbdcurvxbbujfalfjyiafraizbfocrwomniytcipfbuygctnjtvigdvhegeaicuuveynfpjiomilfhfcdcujsmjjfaksfrduucicbjjystrhuqfouyemxciyekvhbbdcurvxtnfluqdyoavluyzhuwglftrcmcumvqgydrvxbkrmbbumuyzltyugjpvumjrhtuvlufvhfyiyswvnmceaufrxwyenbevmqpfmqciivqiynyiebzcsnwzhiyscugeatmiybqfhbzcscczzumfuowrjqcrlbltybleivltcoezgqmjmjzcyplvivrdltkvuoqyybpkbbkkybpjmiycfqmnyscmyswtiorvhucuafructriotrjwfpkujlksoypuscwlblbhfqjwpltybjvxiydioseugdvwuculfqffvrziomewpljceciyemwhpryiveynncyotzrhemiwpjfhfjwiskzhhcwzfakmflumjrkcoejbfuzhhuyitynvfqzxfqjioklmjarfbbrjucuwplklbqkyegenfpvmucuybrrfuciuugfhqgrhpdflucjsnnrnigqyxyjbfdrgjjzytzvfjcmyegwhpccyhyewfgenfpvmuqllqpzmfyecuysiecnlplxgjjvmbljieccuzncuucjbfpvfbrziomnhqskivrccwcugbwuctnfmfbpivpjymdiyrszlfbeibrkbpsxbuquymgtuuccuobcisbznccslbltbfbuutfnipbuijqnbbrvpfpzngyinicivfayuqrvlbrmctgkyekrlsgvxjlznqpvmtcuvzbzmuplmuqglpalljlxvfmyzsyeeocjmfvzmucewfzvfjcmcoezhtrrhujpcgbfocrwommeuohlpflzffyjigqvlwyentgemjqkyehlxhcnbzkrceqcyeqzlxffmfelytruljdkbfpgijlkbjktinnrljqfhfqgydgrfmwwljcextfzjxyjqimjogdzwjcenbrkudfdyorwuwmllbzcyimnfvabcmwsoukzhvrvmbqbjjakoscduonvliygmbpvcofrvjryixfvlhmfxbjcmblxgppvqiwyysmcxdmcffakcoejbfafhtguyscuxjqtiwciyeqfuunrlugvmicnusprhumymuypcoejkvyiyocnbppjytyexqskvfrkyscextgewfpznzaffmctnfbyuqnzhfqjxpgjwplkyorvxtgxbftvlxyphpuduowrfuciuugfhzmluoweissembrzucjvxjkzhvrziopvutmeucjvwpkguogfhtqysqyinjyccuwcybdssmcwnecrfngcypfzzfyjsbbuyeufgblwcsqkafrcyehfsomkybpcskmbytgdjsmmybqyuncugbpicfbvrqcemfzvxiciwpkwisrgosqlcukimgmllugdyumfezcpivprmgyzfmyusvnxlfykytrrgfvvlugfhppdusgrhocjbzmtwbqzioycnfpdcoykyegemfljccjvuobzhiyscugeahypmpieixbfzplunpfrfgmehpunbpniingjyxyjdvqkcdceyxuzhegeajlwcogjbfbfhicjjfybcoejojrrvmcrxwyewfbzzcmpbbngcocjmtnfluqdyoqrsqpvpbgcyemwzflucoetioavumcuhppnutniiwgjcplglptzxfbjibquivzkzvjfhtriclgeaschojpvxxyznjlxqfrfwpkgutqrmtsiyeafgqjzgflkcorvlfqkyebzmdpvnjmeytrzgbrzhhmemugdomykyeygusrdyorjiibvusqfmjlxqicecodzhepvuemwwbjcutbzmuplmuqsyiymcpsiucgccugvmecwydrzpfgjhftvlbrnuucigfkzairfhgmigfbdysgkmisenfblhbzcynciymwssnpnbfltyppgitqvmtgfhufvooncybqzhhqzgqjzwjrpbfplhdmdgplcsgykhfujgbjchfqjzfujoqnfmjlxmvqgcdgfhuufwpsimfqzlqcfjmcnisrysimimfqrxecenjpvmvdwysffqplvxvjcafrsotwuuscwusykjsgewjncyqcizfakfzzpmxcvnocjmemrmnpjnbpkyeyiljtrftssdfakvzzvfjcmytricdrcsosdysmlmpskfjtvxlgexocjmxfrnftvlplnyomfhbbucugfhnyelfolytrrxbnkyeqgcsgkmtckjscjmfbljumuyomkcoejochvwuqjyoqzvmcwyfjzhhqznjluomevxegiydrcsxcuqfjccoevfferhdcuitflnucimbngyugkyzmlltcczegmysrvxpsihfvkxscngvayspsncufiuoikiscduowyymbraffffepfmfryuomlltfvfjrvlbrllfqvhugdyorjuowtioriutrvxtckuxyiykmpmfljyzmlhhlfqucrltaycoyjbzyemjltysgkstmvrupvgjrpbfyuxjrzioqyyswvnufvlfrioufdysgkgsqrfmniikctnjlxzbtfosysfflfqvlgffyjcoejiojrqhyixfltbbrksucdjfpfbdfzfepvhqpfpjbvxumdlfjvabltynyiljyxytriioecspdwwblrxngiuugfhqpfmqciivqeixbvppljbjpvxjkzhvrziojrqbbuspsmcfuzhhrvhfolumjpvfjzywcgouqvjbprnfdrgjjzytkpiobiuxgeatbfiimwzfluyeqkljakfzccyhyewfnvldczpfhfcorllfzvgjqklfqjvzhvhogeatniiqcifzyeuekzlbrzioykbfbzmdmmyscuxjdwcdscnzafhugeojlxqfgevvgcxjlxlfkfpjlxjpqjccjvmvgkucjvzsgvhejpiolrsnguxmckiofzgbbdcurzhhafhtscnfbrhezvbbtzivpjioffotcyimbiydsilfbrxwyewfbyypfkihckbfpvhuprhdcjjfcucmwjojrrvmciybbpnsgvxhypmuykygykwpscxcmpcuqrgplxmiycfxyjxsyncoeeuusiumdrnscjjfakbvqsuobrhbqeijqpuomwzfpulbuevmsjbqjrwfryytckljcuzppnuzhfsxpfnfuznuwzhnpsyhyegvqzwxcvetywnfprnccxcocuodykcpleiecaydrzioqfxjpvwugfhqpvnfluyeffotcyimbuiumklbtvfmgeaftvlzrycoeyyscrnscrmplrvmclhtykcbzcyectctgmymwjcnnccdgksnmihjlxlfolytrsymyjnjlxcudfluseyecduobjbjeyytrfztfvmvqgcdgfhecaydrzioqrqjljnblkfzuvfmbvhzkrsscrfplvnpjusfrjuxfrlebvuszvxdfzygffotciuqguljeynufvmfreijqpiocjnbrvnfyimxfzwilfajpciinrluklmudrwufzaikpbfqzgqjzwjrpcocowfjcyoavgfjrhdfffzyjlfkrllysfzbzmdmmyscuixlgusrzumgksnmkcplcytqnutmcxfvtymjvhdcjbfgekvgvnvbvwplklbqkyeqzmuciajtzhhqfqjabyuafotgeigyebfprnicigbpbyemwioergfnrluzfxzpzwiyuuqrvxnpjuwgeattvhusiyjrfldmdzppkugdzrfbwljcextafnuyxypskyoysffbnutcenfpvxhpvuujpjscmyordytqraflfjsmtoscuoojfwlcuuojzefuzmfbvuszlnxfrntfvvfceiwciabwwymrsiewjcynicoazjmcjuetrhuyxytyexvqvyoriybrzytbvwjqzpfjpybrdyufrmeuvfmgeavlgudivxtcvqiykywcizpjcixcuwpsinjlfzmcrpfyxujlrmbkxlfykysqzrucvhumwiskzhhaffplvfomfhccjiblrxwgtyiyixmwsusrfhicsyusihfbjoebvhflxuhcduolvltnzljrgcrsvxgymivpjnbgimjrvhbzcyfvvnfprmtcvcoeiynyzhecigfrzgqpfpjlxvvrvhhpfmtcumjltysgksbevvfrkyszlnmceaufxuzbvhjcuucpfueyiybrkudfdyorrmumectfvxumfhbngybprhdczgqplxfltytmtimjvwugeajlvrdccffltyugcyeurscjzhejzpfbnbpqvhfukbfdflgscfzfrxtfvniciymcrpfkvljrvhkmpzppkbplvuetrhdcuxjtvlucuxpkvmugtmfviyqcrnfbsljlxcoepivmcxqmjmjzcyqpfwvpvxicinsgwfjlxfbsxbucinimlairjjsmgysrpmicdyuursdmdjblzioqjbzfrxtmccdgkoecwuwmllbzcypueqigtbdmlfeqrqhsvmukrhomnbfyixcskfbqkyekpwpkzhhseybqpgbpbyeqfmimlfeeiuwgksmcknfpjcuydioejnicimfjwxfyiytrrhxgexpujvzufiecufbbzytqyycyjefrjybqfhbevbfplhfyjstynxjqtivpjyvlncmjzhhydhpbvmdpzvfbuykctnjmecoafgnmuyomcctrvhjlxigzvzppvhbrllffzmqyictfsizwvnpkzmfppqjquinncyorpjpjznfrfutniyqyiyegenfpvmuniiqmjumgkbfcoysazmfkpqjqycoerhjlrnucdjudvlsyimwgjcucuybrpivuystcipjavfpmbcoevhhyxyeykjmytyomnumjjbpnvmsmfgtdlfmwzhsmfzimgytfpnppvffywdpwgujbsizlfctgvlpskvsmlairvhuciyebvnsytncctuvqvmjrkcoejcsdrnqskidarmjmelfluyscuigdyonyecuwyutgemjnzxjrpnicjogdzwjcenegjwsckcplzgqplxfltyscjimskcpljcsfzgectctgmymwglpavyeffqblpyoerafbmctgkiscojmyzhfbglpnicfrpigdfounvlqckobjyctwfogcvftmcxpdwzfjkhbwiitcdyuwfoxcjiflklfykcfqtomrzpbrvxbqkiogjbfbzmxyjmjqkysdflgcnfplxyskimtsuxflkumcencctincuiocduzzflfolcucmcmmcxngcyjdcclccsbkfzccrouwkutrvmtgcyorjcsqrsecjcscwuufzgmcknfpnbbrvpfpjyurccoexipbeytqkipyeximeivpvxtfvvvgcxjlxuoqnyscubfpjnsmeamwkbpsxbuqiyncdvfpdlumuidmemjbvlecsuugeatnzljrjgvqzwbjsyiymyemeqffvzbpkbfpcyurvltpvjvjjcwcyyicrmecwcdgvhulvqtnrjfpuutfnipbjqfbzmdmmyscubfpyctnzuomwisrvcoqzjjbznzcenscrnjcjvferhicrnucigtkvuorrmgyewzziybiwutrrlsyeajlxbfgwzvpecusiyxcuytaicccuioyjnplzmicunimiiveyfzsejmcrmblkytnvwjycfzwfoegjjbrtbfbsyedrppsiucjvmpazyuwvrdgkyezpwprkuhcgljtrnfyecucjnfcdmgscfzzvajlfhcwnivluuoezlmpzwigexpsgiszfniykxfacuscucoyjlfhfcdcuigrfafryysfvcnniytqzioaffmctnjlxxfjzairwomsejmcrmblkvzniitnvlpsjutmeyobkiprrfflkmicfvkctnnpjqblkyepvgptvajtzhhfvqflkmvayxbpvapmugsdrwuryytkrfmmnhtcmyoqrpfbduoyxynkhhpmwzfpjotnzwjmexjbdltlflgsihjrllfqdumjeytqjwbjvqimcyemnhtmwnflcybtvhprvuuyeyyniytqziopvutmeucjpwvjkcwykyegexvjxyoavgsfvmvpiivluyegemuplgflkaflkffkrhfykuobtioqzmucuuscglplfooavxjqklvqkmtrrlucubjqyybpkyeyesdgmcmjpmpkvvzkrljyehfyugjrkyeqgybizhhkvhcpvxggeydycfbqbwfyjyplvgjjvmuplnibrsbzfpfqvpfljotnzwjmemqmintkvhqpfpjqzioqlzgcicoedltqrqflxlpqjyeqfgfrycoejhvejiplyyplgfblzhccucocjincfohfknicjybpvvbjcmqjrwfkimufvcsrzgfqrxeqyyuybyolfascrnxguixqgilcfzjrjgbjcaflzotsjyfvtyqrjiocjnfcdgfpvfzfvlmgdcuqjioqgusissemdulcfhjruipftiurrafmwzfpvxdmknbevcouicurvhfqgydgrfmwfzegjmjkzfbpljbrkudfdyorkbfkjymtvmcwzhuciytrvxcmzmuciivqccocegsqjyfkjgflkucjvdflecoejxbqyqpmunpolcurzhhkrlsgrafzrwiccisgeioyjwplmcdrziogeigygjfyiuoavuqyinncentzfctrvlpsjjmcrmfbycnyeiufvlxyjmfrkffbwiskflfmmysceximiljzcyfluybtflflklbltyblpzbkzfjcjcoafgfygjfyiyyrvhumeigrylpuecoyugjpvmuyebjjciouvcgtzwjlznzkrnfpzumgembuycnqdumjvmuwfoqpfpjbvxfajnbrzwtsgjmgvxhyilfrnuorvxfvgydriynyzhbqdldmmyscujbpcisqtioavlouvyyniytqzhwgjcucunpbfwfjvvsykyegdjpqjccjvgzsewpkdiojpjbpkcdscuszpiigensmuodcucoolcfrlxfbfunmeahmzhhkrhppnbpbzxempyjqtymcslbrvxjrjsnnrnigqydmemjbvlfbduzctmuykcdbzxtsijsgjyfjvabltyufvchlflblkuhcfqofvlngjmdmcxmyjnjrjiosdysmlmjdyypskfjtvxegjjpqrfimnvvrjioqdltjrxzuyyofvlfqgydgrfmwrlfsejmcrmblkivrrfuciuugfhdmenjllcoelhscjystvxscjimskcplyyoavbpnvmomzmzkrsdfzhbdlfmwrheydcupvabpumuyzltziuoayniginzjvhhryugdflelfqjluomevhdcuctqzgjjrlgmibjqkbppfohfcsiyjnfpdcoykyeyxlfcdyorfzgcexjlxwpkduobvxnwrhdfrhhcnbpjcstypqiwvfecjnqcicpbrlfniikctnjmejvrtymcslbrvxqyinjalfbplhscjystvxkmpooqrnjysffgkmjlkbfluuscxipbrgsmjycpvxppfhbkzhocrlfpjkvyiyxyenfbnlplxxpnfcorrppguvzdiojrcybpeisgexfykbtmgutqrafffqftvlccjcecjcotznfbtindfluccxfpcsccdyxycftzvablfzdfzfeazpjjrgicrleffjfbdstykctdzyeniyucexfbdlpluieckyskzhfzpimbgitrkipirheyjetcvhgytnsgtbnyeyoriuoavmfrkfjlxvfjzywcuybraizkfhfwrmepzzuzvajlfhumtinnrljqfhvnzhtggcegksfqgydgrfmwuctafpfpvxncfzectctgmymwzhtsilpsexfbgijlkmtgoqbwvhpsxbtfvcuqwuufvlgmcfzqvremnhtrvusqyuneiyflwisrpuoafoorisecdytlvgfqjuhczncytbfjflemdytrzwfvkyobvxemlvudlfbqtioavloqrnnmihjlxjssuyoriynmmumyeffrkysqsspltivjugzgeisbvlocmysgkiscowjrvxdcinbgemjvkyflznumgusrzytaffplvfecgyobzhhafhwcpcoeucsctnjmebbqcyegdgfbzuuccuxernffvlxccfccufjdvzfckmfcelflkiolrnvpvislfyyavjugkmvqjyygxhpprhuqrqicibfpulbuzhhqduspzuhccuveynfptutcfbblkbbrflburstgxbemyyscljplrwvrvhfqjspsvrrszmjrvivpjymtvmomnyobwisdvcucuyoolcscpyxgkbpskcuerlsckmvnycnqvfggenfpvmumllomilfavcwcuzpjcixcuqbqtomrzpbrvxblljtmccdgkoecdlvlgffyjuorzntnfluqduocrlocjnmwpyqpvmfpmyeyeiokfgflkffbwungcstmfhfptuolfniciqjluixnlfmcuuowflsyzfmcisjdzgqpfpfbcuobcisbkitnvulgeaiyjnflvxegwzfpvxicwoslznvpvxjqtivpjyfjjyxfvlfwvnicimjpvrucemjtvxfdvwugmyvlncmjzhhevnxfplfqffvrziomeynmkcplcytqpivfzgufflpsxbmweijqvctpfoobkijlznrszwlrzgfbuippjqsgknflrxepvmteiybrcshckuurrwlqzhiyscunlltsznpsivvrcutrvxisenfbvhpsxbblljtcvcoezhmgmymwcyurvliyudvbxgflkivrfjjlzioqglpnvluwkbfqljqjzyeyemxcigjqvlzyucfsjuebnipbvximnhbwdyozvzppvnimlainiyucexfbsymmeajlxwplkyorvxnpjmvdwysgeagymivpznfwfoufvwplkcosrfnpjwjtzfoypffyjnncrhtricfbuljdkhbrllbjvhejrqxfvnicivvrrherfqbpumdcinbgezvpectfvxvlwyfjzhhfzmtmdyugdytqvyeypjsmdiugfhrsznugeajlwiskvxdmewfpemdyegfleixniikctnjmenpmioqafhwgtnjmeooafgnmefzbvfjeyngscwplkcoszhhgeuqnvnjrvydqkuugtiqgecpljbbqkyocuvzfrheqfgfyugjrkyerfmppisxmifeyeuubfmqmzfbjfhhgewpkdiecyyecgyobzhhbfzsyeeocjmscdujluysrfyeurlebrsbjditrrwugmyigdzsgvherycsrpjjolyenviqjvutnvljmunxcenzkpyyrvhuyjmfrnutzvnuciucpfuefrgqjvhuwjydsiyiyubppjytyugjprnjmebbqjcsbvwjqzpfjpyyavfmcewfqrsftvlzrycoezhiyscugeabatyqrrhdcjiplvltcknmcrxenlnzmlmvbuyofzgbzzfjrzytdflgcznfbjcusrnjmeyyriynccsnwkiiciytcdvmcuimbyueafhwgtnjmexjqtlfrziosexfpjnpmujvrgljltcqjvmzmlgbrtbncrhtivyqqiivluiocyysolcdijbfdflngeauufwpkwisrzhwgkyewvntfvcoafgfcwzfakyeurlecenjpvxfqzlfursecjchlwyxkimtcenjkvhuqcyeqffjaznvbvytrzgbrzhhdicflumiggzbrdyblknimjyftvhugjqfcbmtrrnfgknpmivpwsoufrmgmcfzayuskkbfpvcuqzntdrwurvhtnfnepvqqjrwjlxutqllfbsyjdiynmmyegkvfqzxfqfhgyimicuybaybjeylfyuuscdyommysbrsbdiujbnyqprctcccwccsicjogdvlgydcmwvmuykyjqrgqjvisbvlvnzhpdzhscrxzrzgfbsfjlubbbeixryitcfohfkmfrfzuceqigtbppjhveuomjyytffqnmiyuplyxgjbomrnnyesecesbursngjmftzfplzhtmzhecvxtnzljrrhnmkbfprgpsenfbffeqkljakfzzlnnyicbleybbdcurvxqcfjmcwiskvljqiynmmyscdujlrmbdwlplkcoeuctaiyugfhbquijqrhomlhdgeaomngplkbtcjnfcdiqnfmflvusciyoysffrfitgomiceonciivqlhmmtefbpivnvldczpfqgyfbzfzywzjvvxpdwyoavmqgicuqflzcfzpdwcdcjvfrnyfliybjfhtffnjrnyscwivprhbqrvtmcoucsudfvfppiyobvlfbjcylrszmldvtvhjjvpblznzcenjpvuoayuurpnpzvxtgewfpznzwvnufvlfdflfdflgcznfbyctavluyzhuweyhjvwucukvcjnjmemqsimvgkwiydvfprmfjuysjpunmeatrfhegjnblkbpuvpfpnusprhudrlufvlumfznwaotrzwfuzmigeaqplxflkqbgkcoezhcctinnrljqfhbevhprgcblfzppkyjltlfyjcoeuymgxbudlfomncoqzjjbznzqlzggtcflkxjqguuayyeyesscrmplrvmwcyeyjebleivltcoezzbrkudfdyoriytmcougfhtcenjkvhuqrxngiuugfhncfhegdcoskcplzmqmjnfytbufrnksjnmcrzomyydmehfakcplzhuciytrvxtmnybljsnnrnigqybbmuorrafqkityzxjqzntfvxxyenemfwdyjcplrfnguxmckioqvpfppnigeatmkiiymytnfnqyingmibjqhojrduzceucjvcugjmrsrlfkpuopvabpuigrvhncicuqkogdwcsqkiisgbjjcmbqyytcipblkmdmenfkgnbqrfuffohfrxegkcpluutfnipbzmqpfwvpvxjlkyscjnjlpivpjymdrhemfzosdysmlmgcvfjlxmdfvysdlfdmezjlvxtfvqjlxgfrgusrzyteiuwgksisjvblumfvgffyjyemenplfejluxplvrudvymfvfeurfljrmumnhmmlxblueocnajtvabwwivpjyorzgflkmnmkcplcytqflqpzhdggffqglfdvlfltyfvtymjvhdcrgmgkysykoscjospfoobvxjljyoqzvmcrnjluomevhdcflumrxngiuugfhscdusirvmwduurvlgskoscciwcimecjcscdusivxcmpotctbbksyspvudfvxemyyomkbjlxvfqllsmlhecuugdiiorzhhdrppsiucjvhpkifbgeeocnfjivbbjwmicpyuhfscckbbluomjrmtcvhwcistffnbrkudfdyorpytmrguprpfjccoevmugduugeaqpfdfakcoezmpdwzbrrxepvmtyknbabmigjvfqzxfqjojrrvmcjyurccoedlbrkyobvxomuivzkzvjwyfjzhhqrhzmmysdfltypvppvmvaympjuzjtvvvryooejosnictcjnfcgytriydsilfbcuobcisbdlxyexfpvxbkfoorvxpdtiorzhvgeaecmioqycscsouafhtguyscucuqiitcgutrfbtfvqsmfzjqjioeeybruiecgyobsyurvlqprctcuigpzyobxusbvhblniobvlumzhucenjmeuhceuzmkbfpnctcsouziybiwutrrlpsexhyixflsyzmexumvrucencwwomdzfmcuxjpvwugfhvqvwplkcosrftckbjkglpnicfrpwplkcosvxtyngfrrjqjroecuzbtfosgkyecwcdgvhuceasmjmfbtioavumcuuobyysafhdjlxfbsiznvlqckobjffeqljqmjcoewusryyspvfbrvxccuuobgutqrafafggmindgmcmjpxbqyqpmumtcvzsyeeocjmpzaydrzioyscmgkcfqkbfyjbbqkyocuiiniiestyeniitnvwudflncifzsgunncudgeagmigjlxhbwcipizhhmcxnyiljcuzfuyutkrlhyiyubzmqmjyeyuxtaiyflvxscexfpvxtgombwyctqkljizhhafhggeyeydigkizsgvhejpvzqklplxfznvwvjzushlpflzffsejmcrmblkcuqlzggtcflkmjkgfjaznzydvzdicflumigghpgebbzznjlxapmuhfqjxpssngscgbrvljycbbquyomkcoejojrrvmcjbfrniecrlncrhtfvqbwrhenfisziyeryyzafgffviufvlxgjynczhdmdgpbvyyncujlvxtmzhscdujlzhhnffjrvvbpkiogecuurlnjpxpafoorpfflxniyeungewscrmjlxuuafhuprmucucodrppsiucjvbfafhtguyscuutrfhjqyyeyjcgkrxffvfegeuoqyiuzpcuceiveynptrfmcpxfqzlfbfgsqtbjcwascrnnyzxtryytcnbjayuscyunkrndfjbfysieckiupzyebfnigeanyzxtbfocrwombzmqmjyepvnvpeyepvdpgtyerfxbqyqpmuctqfoqzfnipvmumweomnxsynzplujpqkutgkuhpvyncenecwydrzpfrfyyavfmcengcvvmwuiflxuhcfzoyilpuvrucemjtvlfnlftgmycccioezhhbvjflucoezzqpfgprziozvtfycivqcsbqglfdvlfltyjlhojckoecrmllfqbpvxjqguuayyejvxbngybprhdcjgbjcgfyenjljiemlvuffjfqdytkrfmlvmtgjyygjnfltybrkyobzhhfvyohfsncengymivpznfywzfakcpluymgmyscuctrfsfzvfplxcoevhkmpgflkjscwyspvxbqkiogjbfbrheytwfnkuoavgflkqpbzmdpvnjmefbuvxvarnjmelfafgncexeguichvwugfhimnimbxuwciybblmfursnybytnfnimnhppzheylairvlhmfxocjmblcclcnctcfbdmemjbvlbrglpallfbnuobvlfbjioejqppumxpfhhzpgffzfmqyybpunjkvxiygjzcrnnypxpmimtmeatzvchlflblkmpmwmvgkucjvxjqjobbvqfbucoejnpevniciffyjnxffffrzgfbnyjqrhtkrfmlvmtbvzjazyoructafosqvxplvqtnrjfpsyblvuhcihfqjwplkcosvxnpdsscrxzelytrpybdkysqyisrrnncilzyciocuijrsosqkgfqfhhqjisppyrsrfdfrlnhfsicinimjygmcfzfrgjlkbfweijqduowsiufiydmdgfluhfutiorvhucucorvhugfhjkglptzhhzvxqcizppdyeyxyjkglptzhhmwmpqklblxysqiytmlldcjcoqkuorcsiygjjlvmtykhppkbxyixeyeafpeybpvlmceauffjqmjyscrfmwrxelfqfgkbfpsouyjescxlfrvuuziuoayzbrxusbvhcctincrgicvrdcgnxgjbfqgutrjibruippnyxycexyentstbtyeagcvfjlxwpjfhfjxyufvlhyilfrjixlgusgjbtmvhbzcyjleuuczhgmigfbdctqvxiyexuufqbqvuuzlmzdrcmqkuobjgbpkasymyxmlfegempzvudavjuyewfykjsctuvrzioyjnplzmicuyyavfmcewfryismlaijpctcenscrnjcjqimuydgjcwccsbrkudfdyoryutbzmqykwicuzssznecwysgejbpksncsojjkoobvlggimudflcyuyigdvvrjuwgeatqvhegeaiydaflvlbjjiqjrsemzhocrlqyieufrnqyzhvqvmfalljlxwplwcocubjqjbvrkysquymgxbudlfbqyyjrrwdcgnbltybljimgtcusuyegjwsckcpliybqfhbzcsdyiljyxyxcyotzrheqrxwyewfbrhqciwfgmyhpvuucjnumkumjpxfyiytrvrqcemfmexfkvmocpyictosgfmjrpyyavfmcendmdgbluyegegfsejmcrmjlxcnniytqzioryynqvfwcjnpykutqzmuyewfytwfnkuoavgzmiioafhtguysjrohfkysazpjjznzmwzfluyemycofrvjryybpzhhnvliygmplpyemeijrdujbjxfarsbqkbfpvbfqdumjvmumemvgkucjvxjqgitcuxpycnimlaizcytqzhhfvdvtvhjjvcoqfwjcksppzzfvtcucuzppsuecyysceuncfzgwvntfvfplxmpjuybqpqimdxjdwyscuiiayyfpwomniidsiyencybqllfqvwvpzhhqlcuysffgebpjuljayioyebfmyzjlvwiygnfprvjjznzqysocjmbpkcdjvqfjtincsyemfhtcipjavwpljceciyeyecotznbrziobfcoriiestyeqlzggtcflkoobvltrfiegemuplgflkcumwxfazmjtvfzdicflumiggcoyjwpjcydrzhhykhpywzjvvxccyotzrhewvzfkrffqslpryyserlsckmqpfwfcuffyjndfzfeuyitcmyofrjqwpyuzrfmqpivlxxjqtiwcistuvyulvmtnicoazjmcuctafosqvmiydymcjmccuiocvrdccfflkmflkcncentmwmvpiivluyedicflumiggxjqguuayyeafhoctnjmectfvgfmijsmuodcsytguytfrmugcsvnrmqjvutcuvppvffqjqicebbbrhehfboqyyeffjfyemxcigjqvlzyucfsjuebnipbvximnhbwdyozvzppvnimlainiyucexfbsymmeajlxwplkyorvxnpjmvdwysgeagymivpznfwfoufvwplkcosrfnpjwjtzfoypffyjnncrhtricfbuljdkhbrllbjvhejrqxfvnicivvrrherfqbpumdcinbgezvpectfvxvlwyfjzhhfzmtmdyugdytqvyeypjsmdiugfhrsznugeajlwiskvxdmewfpemdyegfleixniikctnjmenpmioqafhwgtnjmeooafgnmefzbvfjeyngscwplkcoszhhgeuqnvnjrvydqkuugtiqgecpljbbqkyocuvzfrheqfgfyugjrkye"

vig_instance = Vigenere("keykey")
encrypted = vig_instance.encrypt("message blabla message blabla message blabla")
decrypted = vig_instance.decrypt(encrypted)

decrypted = vig_instance.decrypt(cipher)


length_of_checked_part = 10
for i in range(0, length_of_checked_part):
    for j in range(i, length_of_checked_part):
        if len(cipher[i:j]) > 3:
            find
        print(cipher[i:j])

# print(encrypted)
# print(decrypted)
