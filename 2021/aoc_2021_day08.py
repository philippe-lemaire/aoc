unique_patterns = {2: 1, 4: 4, 3: 7, 7: 8}  # segments:number


def get_small_signal():
    signal = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
    return signal


def get_big_signal():
    signal = """fdceba bafdgc abeg afbdgec gbeacd abced bgc fcdge bg bedgc | bafdec cgefd gcebd ebcgd
gbfac fegbda fcedagb bea ea abcdef dgbfe gfabe dgea gbdfec | gdea bgefdc bea efdbg
eg dagef gbcfeda ageb cegbfd gfe dbefa facdg abfged cedbaf | befda daefb egf gcdfa
edgacfb gcfd dgb degfab bcega bdagc cgafbd fbacd gd fceabd | fbdac gd gdbcaf dgb
eaf bedgaf dbafc bfceag fedcbg eafdcgb debfa ae adge gdebf | abcdfeg febdg ae daebf
afbdc aefg ea edbacfg dbefg eab gcbfde abecgd bgefad bfdae | gfea bfdea gbdef fcdebg
deagf daegc dcgabe abcgdfe gc cabg fedgbc cdg dcafeb ecabd | ebfcdg gcade cfegdb dcg
agecd bdegca cfea af abdgef fbcaedg gaf dgcfb fadgce afdcg | fadgcbe ecadg bgefad fag
degcba cfbge cdgaefb gbecfd ae gafdc gfcaeb beaf cae cefag | feba abdcge becagdf bagefdc
bfcga ecgdbaf facedg cdfae abecf eb dbae ebf ebcdfg cefabd | bafec ebf afdce egadfc
cfaegbd adbecg ebgca debafg cdfge fa afg cafb fgaec afbcge | gcbaef cdfeg efgacb gaecb
efacdg egdbfca bcdagf ceadg dface daf bafec dfeg fd cdgabe | efbca cdgae daebcg geafdc
beg dgfab geaf gdeab fbcagd efdbcag cbdefg edbgfa ge baced | gdfab ge gcbdfa badfg
gdab bfdeca bgfeac becagd abegdcf edcgf dcb edbcg bgcae bd | dbegc dfbeac cafgbe db
cefga dc fedcgb dcf fdabe ecbfda dcfea dabc debgaf bfgadec | gafec aebdcgf agdbfe cfega
bfdec gbac bda dagfeb becdag cagebfd agecd feacgd ab cdaeb | ab bacde ba decgaf
dbg ecabg gacefd dbaf agefd gebdcf fdacegb bedga fgbade db | dgb gbcefad dbg bdagef
fbge gaedb eg dbeacf dgcafe gedabfc cdgab aegfdb dbfae ged | dgcba abegd bdacg begda
abefg ad gcebd dae dfbgce bdeag dgacfe dcab cgafebd geacbd | agfbe ebcgd dagcbe egbda
gdcfab cdeafb fg dbeacfg gcafe cbeafg gdcea ebcfa gaf fgbe | acfeb fag dcgae acfbgd
cegfad fedb fbgadce bacdfg acbeg bad fcdabe debac db cefad | fdgcae cfgdea edfcab cefad
fbg bgec efbac fbgca gb fbcdea bfdgea bdcagef fgadc cbeagf | fgb fegdba fbaedc aefcdb
aecfd agcdfe bdegcaf efbad bfeadc eb aegbfc dcbe bef dbagf | bcfead fgbcea eb aefdb
gedab cfdbg egca dfegab gedcb fdebcag acfebd ce cbe decgab | acdbge bfacde bgade cedabf
edfg fbgdae bagec feagb fbg abgdcf dbefa bdeafc agfdbec fg | dfeg daebf dcbfga gf
bcgaefd cfbeg cdefgb fcde adgbec acgbf efb gebdc fe dabfeg | abgcf aegbfdc bedacgf edgabc
dgfbc bfaegc fad dcea adcfg edagbf da eadfgc cdafegb geafc | da fcgad gdbfc afgbce
cdea bafdgec gcbeaf bcafd fdbga bcd cd ecfba fcebdg efdbac | dfgebc cbd fcbad cdae
afcegdb edagf ab gbfce ceab gdfbec fdgcba gbeaf gab cgbaef | ecbgaf bgafecd cbea gacbdf
efgcab ecb bedf be cbfgaed bcdea cdefab ecgad fdacb gafbdc | adfegbc gcafbe fcbgae adecb
gfecad gc egcf afcbgd ebadcf cag eagcd acefd bagefdc dgeba | gc acg dcafe begad
dacgb cbadge dcf cf cdbaf afgc bfeda dgfebc bdafgc feabcdg | cgfa dbagcf fcag fagc
fgb fcabd fdage bafegc bg dgface afgcedb adbgef dfbga bged | abfdc ebfagc agbdf dcfegba
afd cdfega cdbgfe bgefad dfegc becfa feadc bcfdega da agcd | deafgc fabce da gbcdef
fcdgb baefgcd fe dgeabc ceabd fde eafc febcad defbag cbedf | bfedca gdcbf daceb ebgdfa
cbgf bg decafgb ecadgf dcagf gfabd bgcafd gbd cbadge dfeab | cgfb edbfa dbagf gbd
bda dfgbec efdga cagb bgead egcbad ba dfceba degcb egabcfd | gfead ba gbac egbdc
bd dab cbgdea dbge bcdga gdcaf fbdgeca abgce abdfec cbegaf | abd bd gebcadf dafcg
faegcbd bdagcf cdgbfe cb efbdg gdafbe bdc aegcd becf degbc | bc cb fgdabc bc
cfbae bcfged cafdeg fa acf febcg fegcdba bagf afcgeb dabec | cfgbe egdafc fbgdec cbfea
dabfgc gdcfbea cedaf gebda dagfec ecbf beacd bac bc cafedb | begda bc decab defcga
ecd decgf gebc ec dcgaf cfaebd efdbga afebdcg bfedcg dbfge | dgfecba cgeb bfdecg aedbfg
efb afbgdce fdceg aebg afcbg gdfbca efcgb be dcbfea fagebc | bgfaedc afbcg efdgc cgfeb
eb adcfeb eab dacbg gebcfad gaedb cgbe gafde gedcba gcfbda | abgde bgdae daefg cfbagd
cdfeab cgfead bfgdca bfgcead dfcea bdeaf aedgb bf becf bfd | cefb dafce dcebaf edgcafb
acfbegd bf gfb cbaeg gaefd fegab cafb agebdc bfgdce bcfega | fdbgec faegd eafgd gbf
eadfg gdc fegbcd ebdfc debcga bceafdg eadcbf bgfc gecdf gc | dcfbea debcf gdefc gdc
gdb afbdgce gb gfdce dacefg edbfcg bdaecg fegb bdafc gbcdf | cfdbg dbfgc fcdegb debcga
bfcdg befcd efgb cgdbea ceb eb fdeca efgcbda dcbfag dcebgf | gfbcd ebagdc dabfgc dfbgc
acefdb afbgd cda ac adcgfb bdgeafc gcaf gabedf bgdac ecbgd | gfbdac dbgca edacfb dfeagb
cfadb dfcgea aebdgf ba edfacb eafbdgc baec cdbfg abf cadfe | dgcfabe aceb edgcaf afdgeb
cgfda ec cgdbea gedcabf dfgcab egcf beadf dfeac ecgadf eca | gfcbad feadc fcead gcafd
edgfa gfbd bg adfcbge agfbde edcgfa abfec abecgd eabfg agb | fcaeb dgcefa facedg bdgf
db eabcdfg gefcda cbegdf dcbg bdf gedfb edcfg fdecab beagf | ecfadg cgdb bcdg gcfead
dbeca cdbafg gcdaeb ec feagcbd fdbea cbe gdce bdgac abefcg | cadbg dacbg cbadg bagcef
cagbfde gbaec cfbage fa bfcadg efacb ecbadg cbfed bfa afeg | gefa abcef dbfcga fbeca
cdefg degacf dbfca dfcga cedgbf fdgaceb gaed gca ga gcefab | ecgdbf gedcfa gdcef gcdef
abcdgf acdge eac ea dabefc aegdfbc edcfg cebdag abgdc agbe | aegdc bcgad dcgfe fedacb
egbcdfa becaf ecbdaf dcaf edabc cbf fc ebgfa bgdaec bdefgc | ebdcfa ecbfa fcb cbagde
bacfed ecagf ad gadfe aed bdga fdgbe dfaegb gdbefc dbcafeg | gafec gfdeb fadbcge dcegbf
fcdgbae bgcadf bged eabdc ed bcadg baefc acgdfe eda cdgbae | fbgcda bgcad faceb eagdcf
fbcd ecfba aegdc dab bceagfd fbdeac db afecbg decab fagbed | cegda bd cgeda bd
gcdeab gbedcaf gefc defba ced faedc cbgdfa dgcaef ce cgdfa | abgcfd cfgbad cgeabfd dfcga
ba gfdbac bdgecaf eafcb gface bfa eagb cgefad dfbec bfegca | ebacf ab gdafbc cgfeab
feadcbg fbg decbag ebgdfc faebdg dabeg feab fb dacfg fgbad | agfdc gefcadb gdfba gfcdbea
bcgfead adecfg dcfb dbg agfdc egcab fdgbac bd gdbca gfabed | bagedcf gebca fcadg gbd
adbfec afgecb edf cbefd fegcda deab cfbgd ed cebaf cefbgad | efbcd fegcda bfdacge fgcbd
bf gcabdfe adefg fdgab adbgc bcgade efagbc cfdb bfa bcgdaf | abf fba bdgaf fagbdc
fgeadbc bfcgd dcga cd bfedca abcgdf badgf fcegb daegfb cdf | cfd dc bdgcf gcebf
bgecdf geab abd begdc defcba agcbd ab becagd dcgaf abfcedg | agfdc bda dab dbacfe
egca gcf aedgf gc dbfgae gebdfc fecdga adbfegc dcbfa afgcd | gfeda deacgf ecgfda deagbf
cdfbg dafb gcbde bfc aecfbg fagdc agdcfb bf bgcdeaf cagdfe | ceafbg adgcf gdecb bf
geabfc ecgfa fgebd dgeabc aedgf facd fcedga ead da fbecgad | degfa cdaf aed bacdeg
dcg cbde abfgcd fcgeab gaceb dc dacbgef cgaed degfa degbca | dcfabg dacgeb debc dcfbga
agc fcgdaeb gdba dfabc fgced gecbaf efdcba agdcf gcadbf ga | cdefg fcebag ebdfca fcbega
feabdgc badef fg acfbdg gfed afbge afg dbeafg begac bfcead | fedcab fabge agbefd fcdbae
bfcead cfe bdgafe cadefg fbdc bacef cgeab fc dbagcfe fbdea | adgfce cfbd cdfage fgacde
cedg ebcda ebfcga efdbag dcfba cgeba de badcge eda fbcagde | cgaebf beagfd cbgae efagbd
cfead acegd cedbgf cdafgeb dcebg dabcgf acg aegb ga eacbgd | dcefa agdce ga abge
ac bdcgf acbefgd cgdaf fdgbca dbcefg bgecaf cbad cfa gfade | gaecfbd adbc fdcgeb adcb
dcgebfa fcdbg adcgbe bdfcae dec abcfe ed fcebag ebfdc defa | aecgbd dgcfb gcbaef bdfgc
becdg ag dbcfge fadegb dga ecgbda dgbaefc cafde gbca gaecd | agdebc bfegdc dcafe debfgca
debgfc dcbaegf dbg afgcd fecgb acbdeg bfgace gcbdf db bfed | fbed bgd db dfcbge
dcegba gebac adfcg egd debc debagf agdec ecbfga ed fbecdga | dfbage deg efbadg fagceb
cf dbfgec bfedac bcf egfc bdceg dbaceg fabcdge gbdfc gdabf | cfgdeba dgbcf cedfab cbf
gaedbfc bdfae gfe fdgeab dbefg gcdeb fdbeca fg efgacd agbf | feabd fdegb dbafe bfead
fgbce cgdfa ab gdbfea cafbdge cagfb cdgfbe ebgfac bace bfa | ceba afcdg ecfbagd efbgac
cedgf gc gedaf faecbd dbfceg dcbg cge efbgca bfcde fcbdgae | eafgd cbgd fagde edafg
dbgfc dbfce de dbe cbgefd dafbcg cabfe debafg fceadgb edgc | abefc cbfadg bcdfe cdeg
fabde db fbeac dbf dfega ebcfdag cefdba cdbfge dcab gfbace | dgefbc bfd db dacb
fgaedb ecd dcbfe edafgc dc bgefc edfcab dcba afedbcg fabde | bgcfe fgaedc cd dfgaeb
adcfe dbcga eb dbe bceda cafgebd aefgdc bedcaf fagdeb fbec | abgdc bde deb bcadgef
dacgf gafdeb ag cabfdeg bfdac dbfcge gdeacf geca afg cdgef | fcgbde cegfdb fdecga degfc
fc cbf gfbadec dabef cbfda acebgf gdcf bfgcda bagdc gdebac | gecabf dcgf fbc cdgf
cbdafe fdabe gdafcbe bcgade adcf dfegb abd agfbec da febca | acgebf bdfaec adb agecbd
ebgfd fdgcbea dc gfdecb edgc dgabcf afceb dbc bgdfae cfbed | dcebf afebdg adcfbeg gbefdc
faecbgd gd gabd cdebg dbecf deg cagfed bcaeg fcgabe abdceg | cedgb gebdc cefgad aegcb
de gbedf dgcebfa gbfae cbde cbadgf dcfgb fedcbg edg cgafed | fgadce daegfc de eagbf
gadfbc ec bagcf edfacg begfc ecab gdbef cgedafb ecf bgfeca | fbcga dgecaf fce cbea
afe abdfgc egfcbda gabcf edcafg gcfeba acefb abeg ae ecbfd | degcfab dfaecg gdafbc ecafdg
acgdb fbgd decfa fg bcegad gfa debfagc gfcbae cabfgd acfgd | bdcga dfgca dagcb cfabgd
gefac ecfdb acdfbe adfegb gabefcd gd dbcg gdefc cfdebg egd | gdbcfe decgf efdgc gd
adgfe gfcdeab fgdbea aefcd dfbgec abgf eag egfbd cdbage ga | fgdcbae dbgfae bgdaef edgaf
bgfae degb cadbef cbagfe dba db gcabdfe fgbad dbegfa gdacf | adgfb dbgaf fcedab dba
fb cabdgf becgda bgaf gbdfce dagbc cabdf bdf bfagced edcfa | dbcfga badcf aedcf bagdfc
bdaegf ebgd gdfeacb gd gafbc agd bafgd ecgadf fdbeac dbfae | degacf egdb ebadf dfbeagc
dfecg bdceg dcbafg cafgedb begdca gcf afedg gdbfce cbef fc | dcfgbe egdabfc cfg fdega
dgfcab cdefga fcebdag cb bcd abcg dfagc bgfcde cadbf dbfea | bcd fdcbeg gedcfab gcdabf
edgcbaf gcaf dcbfeg edfcg adcge dceafb cfdage dbeag ace ca | dcbfge fadceb cdegf befacdg
gacde bgdac gdcbaf fdagb bdc cfbeagd bc gcbf abcfde fbedag | dabfg eafbcd bgcda aefcbd
ebdcaf cegbd afdbceg faeb cgdefa bfced ef cbfda cef bagdcf | dfebc cfdbag ebcfd aebf
becgaf adceb decg cad dcafgbe efdba fdbcga bdcaeg cd gebac | bagce dac gbcfad adfbe
dcaeb geb dgcfb gbafec ge eadg daecfbg ebdacg deacbf ebcgd | dgcbe beg adbec bfadce
bcfega gcdba gfcab cebgd bdcgafe agd afcd geafdb ad dcagbf | fdca agfbc fadbeg gefbca
cbdea ecbfd gecafbd def ef efcg fabgcd agedfb bdfcg egbcdf | ecbad fbgced bcfdg fde
ebgacfd gbfeac gcbde degac ace gbadce gfdac fgbdce ea abde | fdgeabc bedgca ebdgca bdegc
ca gaedfbc cfa dgfabc bcdgf fbdgec geadf agcfd cbag bedafc | fdcgb bcefdg gdbcf acf
fcg bcadf cg cfgbde gfbca ebdfacg geca defabg befga acbgef | gfaecdb gbfca fgc gebfa
cafegb dc gcd dfacg cefga dfagb cade bcedgaf dfcgae bfecdg | cbedfg ecad cd cgaef
dfcba ad gbdafce bfgdc fgebac dacebf dab dcae gebfad bacfe | bcdfg caed ad cbgfd
abfegc dbfea aedfgc fdcag cdbg bc fcb fgcdba cfegabd cfbad | fdcab fegcab bdeaf bc
bcedf abdec ae daegcf gabe bdcga facbdg daecgfb dae edagcb | dea cbdfe bage ea
eagdfcb adceb dc fecagb cedgab cbeag daebf dgbc adc acdegf | dbgfcea cbead gbfcea geadcfb
ebadg cdb afbgced badgef bgacf dbcag daec cbedag cd gfcbde | baecgd acfgb adebgc fbdcega
ceagf egdac aegdcf bgeadfc edc afbecg cfbdae ed gedf bgacd | cgebaf fegacb efcagb ebafcg
adfgbce acgef adbgef egcfad cafdb cafgb fgbeca gfb gb bgce | bedcafg eacgf gfdace gbf
baefgdc deacfb egfb gdace bcaefg bg gba aegbc eabfc cdgfba | caged dfaecb gbef ecgbfad
ca edgacf abdgf gcefba dace gca ebgfcad bdfegc agcdf dcfeg | adefcg fgcbde afgdb ac
cdafg gdf agcfe fgaebc df dcabg dcfbge acgdef fead gfeadbc | gdfac gcdab fd fagec
bedag dbfca gdfe gedfba baecgf fe efa dcgaeb defba efgbadc | dgbea bagde aefdb abedf
cabegf ecbagfd aebcgd dg cbgad gaecb dcge cadfb bgd ebfagd | cegd abgcde gdb afcbd
abfcd agdef efc bdafgce ce acge gdfcae efgadb efdgcb edcfa | acbdf cfabd cafde gfdeba
egca bcg dfbaec gefdb ebdac cfbgad cg egcdba becdg bfgecda | ebgacfd becdg ebfgd edgabc
bfaegdc gfeda ecg ec bacfg cdae aedgcf efgac egdcbf begfad | gabfc adfge afbcgde fbgca
gacbf adgfbe gdcbfea bcgfea bdf agcfdb cdegb df fbdgc cadf | cedbg gdcbaf gecbd cgdafb
fgbac fbgad gefcba dbeaf abcfgd dg fdg bfdagce gadc fcebdg | fbdea dbegcf abfgced acfdbg
gae cfabg dbceg fabgced ea fcbdag ecfa aecbg bfcgae faegbd | aebgc eafc acgbe bcfadg
fbcad gcbefa acbfdge ecgd cegabd ec dbage aefbgd ecb cbaed | ecadb agebd bgdaec decg
begac eg ebcfa fgbdca eag gcabd gdcbefa adebgc cged dagbfe | eg eagcb gfacbed cgeba
gfcdea dbeac ebc bdfceg gfecbad bega agdec bcadf eadbcg eb | cegad cdaeg ecgad gedac
efbag egfdba agbd fdage gaebdfc daf gceafb cdegf da afcbde | abfge abdg begafc ad
ceda gfedac ad aegfd egfcba edfgb agfec agd gafbcd gbcdafe | gfdeb ebdgf fcbgea aedbgcf
fagb cdeag bgfde af afe dgfaceb feagd cabfde bfdgec adbfeg | fcbegd gfaed fea fea
efcbdg fdagcb de cefba fdcgb dfcagbe fed cegd gdfeab ebdcf | ed gced cdeg ebfgda
cbdeg bdgac bca aecbdf bdgfec cafgd acdebg ceabgdf ab gaeb | gaebdc geba cbgade ebag
gedac afcgdeb begc bgaecd fabdcg cga efdac eagdb cg daefgb | dafgebc eacdg gc cbeg
gaceb bgefca eg bfeg age aebfgdc ebafc abcgd badcef gafdce | bfcage bfeg fcdbgae gabec
ebgdcf aedf gcfda gefdca eabcfg dgf fd agcdb ecfag fgbeacd | cgdaf gdcba feagcb fdg
efbag efg ge fdgab befca dfbaeg gdae afbdgc gedfbc fgdbcae | ebgaf edfcgb fbage fge
gaefbd bf agfecd efadg agfb dbgef ebdcg acefdb feb aegcbfd | egfda gafde gbfa bfe
dafebgc bfdecg cdaebg da gcdbe dab bfceda adge bdcga bfgca | dcgbae da cagbfed daeg
ba gcfad adbfg fabdeg dbfegc dbcgfae acdebg aebf bdgef abg | faeb bdefag cgeabd egcabd
gafb ga fdcgba ebcad gbfcd deacfg dcbga cfegbd agd agebcfd | gecfbd cfbegd cbafdg cegfbd
fa fab cfbea gbeac cefdb cebagd cdegabf cgfa dabgef faebcg | abf efcab bgaedf gcaf
cdafeb bg aedcg gab acbfedg gbfd bfaecg bcfda gabdc gdfbac | bg gcdae bgdcfa fbgd
afdgc gefbda ebfc dgfec dbfge cbdfeg gadceb ced ce dbfcgae | ce edfcg bcef dcgbef
egbafc fdag ad dcbfaeg cgfba dfacb baecdg dac gcabdf edbcf | fgabecd bacefg agdf befcd
dcefgba edaf ebafc gbecaf de cedfgb bdace cbfead agdcb dec | gfaceb ed gcbad begfac
dcea aefdb eaf badcfg ebfdg beafcg ae befdca ceafgdb bacfd | aef dfbea fdgabc afe
ag bgac dgfebca gea gdace bceda gedcab bcafed egcdf ebdfga | cabed bdeac dcfeg eadcb
eacbf ecabgd abcegfd cbage agdcef dbge bgc bg dgfacb dagce | cagbe cebdgfa edacfg bg
abd db cdbefa dagfeb dceaf fcaedg cbade fcbd egbca abfcdge | decab aebcd cafbed cadbe
gdefb deg bfgaed ebgaf afed fgbcd fbedgca adecgb ed gabfec | fdbcg faegdb fgbae egcfbda
decf dbfgce ecdfabg acbfge dbe dfbeg fgabd fcegb bdagce de | cegbf bedgf de fadbg
abgedf cbag fecgd ebcfg fcb bc cebfad abfcge egabf bcegdfa | egfdc abcdef fegcd cgefadb
cadf feabc da cbgafe bfcdea adb bdagec bfdae bdcegaf gfbed | bcafe adbegc cbfae defcgba
bdfe db gcdbfe bfcag edbgcfa abegcd fbcgd dfgec gbd adfgce | dgabecf dcgfe db gcfdb
acf afbceg dbfae cf ecfba abdecgf cgbea gcef fgabcd dbaegc | cfge afedb aebcg gdbcafe
dgabce fbcea eafdbcg fdcg cd fgdecb fedgb afdegb dbc dfecb | cd dbc aedfbgc cdegba
fagdbce abd fgbedc decfb bfdace baedc ebfdag agdec bcaf ba | daecb acfdbe cadeb dba
dfceb bcfedag gbecdf dgfe ebdcaf fg fcg cafdgb ebgca gfbec | bedcf dcefb bfcaed abdefcg
gcfba badegc bga afbdcge ag fgebc bfacd dfcegb bafegc faeg | gedcfb cadbf fbacg bcgefd
cbg aedbcf ecbgfda cg fgcdbe ecfbd bcegda afegb bfcge dcfg | fbdce gc bcefd gcedfb
dgbcf ebgd fgdbca agdfec bdfec ed efcgbd cdgaebf fde fabce | fedacg cdbgf ed efabdgc
eafgbcd afcgb gbfcda gecabd efgcd acgfeb gecfa ea gae feab | edbgcaf dbgeac gacbf beafgc
acgfdeb cegabf beacg bacfd dbcea gacbed gcdbef de edb eagd | de dgcbfe ed daeg
defa cdbagf bfa agbfced cfbegd efdgba egbaf egfbd bcgea af | fa fbadcg gadfebc cafbdg
dgebcf degab afed gafbd gabfed df gdf bafgc bdcega daecfgb | cebfadg debga abgfd abgfecd
gdeca dcegba dcagfe ageb acefbgd egdcbf bgd adcgb bg bcadf | fgedbc gbdcef ebag gfbced
dc edbgcaf cbadf fdc bfdgac bgadf cbgdef fdageb ebafc adcg | dgbaef dfc bfeac bacfe
eagcbdf caefdb fceda egfab bdca gbdfec efcdga bc ceb eabcf | bface bc bfdeca faecb
gadec becgdf aedcb gfcdae edagfbc dg gefca acegfb fgad egd | cdeab fagec gd dcgafe
abdc cedag cd fabdcge agebcd gdeab feagdb gaefc ced gdbcfe | baged fbceagd ecd edc
gcadeb gabed gfab bdfec abfged fa ecgafd fad gfedcba dbfae | fbced gbaf aegcdb acdgef
df bcgfe fdb beacgd gefdcab fead aefdbg fbcgda edabg dgbef | efbdg gdefb eafd baefdgc
daec bfgde gedabcf bgcad ae dbgaec age afcdbg dgeab cafbeg | eag beagd edfbg degbac
fgbcad agbcd aecbd febcgd fdagceb gdc gc gfdba cafg gaedbf | geafdcb dgefab ecabd dcaeb
bfgca febag dgefba egda efcbda eab fdbge ae egfcbd gacdbfe | aedg efgba dcagefb efdacb
bdagec ecbfa daebc gafcb cgdfea efa fdeb dceafb ef gcfdabe | efcba cabged gfabc fbacde
fe gfabe dbaceg aegcbdf dfcbea fcabg deagb gfde edagbf efa | aedcfb efa afe fe
adfceb eb gdeb fegbda bcfagd fbe agbdf fgeac gafeb defbacg | ebafg feb agfbe bgde
cgdaeb ade agbcefd adfecb febad aecfb efgabc fadgb ed fecd | acbgef facbe cgbafe deabf
bfc fabdgc agcbe dfeac fdabceg ecabf fb bdfe edfcag bdfeca | fb cadebf gdabfc cfbdga
cfbdge adegfbc cdgeab fbg gedf baecgf bcfda fg cdbge cdgbf | fdge gbecd egfbca cfadb
dbcfeag gecda bed eb dfcab abeg agfced dcebfg adgceb abecd | be gabe bed fbdac
fbagec ecfga fgdac ec cbfe agbef gce aefgbd fcgbdae gdaceb | fbadge cfgda gfbace egcaf
bdcfge cbaefgd cagbde fecab fdecga gafd dfe fd gdace edafc | efd daecf cdaefg eacbf
cefgda daefc agecfb fce cgdbefa dfcga dbaef ce badgcf gced | fbdgcea ebafd gdefacb fdcag
ebagd fb fbgd cefda ebcagf cgfbade afegdb bdagce bef badfe | ebafgd bfdgea ecdfa bfdcega
gcedb fdcb aebgcd bf fcgabe cfbaedg fdbceg bfegd aedgf gbf | bfg cdgeb fdebg cebdg"""
    return signal


signal = get_big_signal()


def find_num_uniques(signal):
    lines = signal.split("\n")

    outputs = []
    for line in lines:
        output = line.split(" | ")[1]
        outputs.append(output)
    outputs = " ".join(outputs)
    outputs = outputs.split(" ")

    counter = 0
    for output in outputs:
        if len(output) in unique_patterns.keys():
            counter += 1

    return counter


print(f"Answer part 1: {find_num_uniques(signal)}")

# part 2


def get_key(val, my_dict):
    """function to return key for any value"""
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


def get_output_value(line):
    """Function to translate the line and compute output value as int."""
    # split the input and output part of the line
    input_line, output = line.split(" | ")

    # I need to treat the "words" in a line as sets of letters, as the order of the letters doesn't matter

    sets = [set(w) for w in input_line.split()]

    unique_patterns = {2: 1, 4: 4, 3: 7, 7: 8}  # segments:number

    # find sets that make the unique patterns (len = 2, 3, 4, and 7) and start feeding the translator
    translator = {}  # real_digit:set of letters

    for s in sets:
        if len(s) in unique_patterns.keys():
            translator[unique_patterns.get(len(s))] = s

    # find the set that does the right side pattern, ie 1, to discriminate later
    right_side = translator.get(1)

    candidates_0_3_9 = [s for s in sets if s not in translator.values()]
    # 0, 3 and 9 all use the right_side fully, so they loose 2 letters when you remove the right_side pattern from them
    # let's make a list of candidates that match this criterion
    candidates_0_3_9 = [
        s for s in candidates_0_3_9 if len(s) - len(s - right_side) == 2
    ]

    # we can filter down 3, 6 and 9 : 3 has 5 bars, the other 2 have 6
    candidates_0_9 = []
    for c in candidates_0_3_9:
        if len(c) == 5:
            translator[3] = c
        else:
            candidates_0_9.append(c)

    # here we make a new set, that will help us discriminate between 0 and 9: the diff between the bars of 4 and 1
    discr_0_9 = translator.get(4) - translator.get(1)
    # 9 loses 2 bars when you remove the discriminator from it, 0 loses only 1 bar
    for c in candidates_0_9:
        if len(c) - len(c - discr_0_9) == 2:
            translator[9] = c
        else:
            translator[0] = c

    # now we only need to find 3 more numbers
    candidates_2_5_6 = [s for s in sets if s not in translator.values()]

    # we can filter out 6, it's the only one with 6 bars among 2,5 and 6
    candidates_2_5 = []
    for c in candidates_2_5_6:
        if len(c) == 6:
            translator[6] = c
        else:
            candidates_2_5.append(c)

    # for discriminating between 2 and 5, it turns out our old discriminator for 9 and 0 still works
    for c in candidates_2_5:
        if len(c) - len(c - discr_0_9) == 2:
            # 5's pattern loses 2 letters if you remove the discriminator
            translator[5] = c
        else:
            # 2's pattern only loses 1
            translator[2] = c

    # finally, translation of the output. we'll do digit per digit, so as a string for now
    digits = ""
    for w in output.split():
        # make a set of the "word"
        s = set(w)
        # find in our translator its key, ie the real digit
        digit = get_key(s, translator)
        # add it to our string
        digits += str(digit)
    # turn it back into an integer
    digits = int(digits)
    # done
    return digits


# make the final tally
result = 0
signal = get_big_signal()
for line in signal.split("\n"):
    result += get_output_value(line)

print(f"Final result: {result}")
