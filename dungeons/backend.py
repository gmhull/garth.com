import numpy as np

def get_known_img_encodings():
    # Copied the image encoding of a picture so that we dont need to run the process each time.
    known_image_encodings = [
                            ['Bjorn',np.array([-9.64986458e-02,  1.12657592e-01,  2.17788871e-02, -6.21140003e-02, -1.05219923e-01, -1.02882981e-02, -3.74366157e-03, -3.05749029e-02,  1.35635316e-01, -7.37942830e-02,  2.08169758e-01, -6.64644316e-02, -3.16639125e-01,  8.08780361e-03, -1.34239569e-02,  1.03736065e-01, -1.62208483e-01, -1.75880000e-01, -6.50231540e-02, -1.24842808e-01, 5.92762157e-02,  2.28785276e-02, -4.72231545e-02,  8.48146975e-02, -9.49162245e-02, -2.90826946e-01, -8.38090554e-02, -1.55835561e-02, 2.81401947e-02, -1.88960537e-01,  1.11517057e-01,  9.46665779e-02, -1.68795809e-01,  1.93080474e-02,  4.56023477e-02,  1.36379033e-01, -1.30885512e-01, -4.72614355e-02,  2.42800146e-01, -1.23159084e-02, -1.15754418e-01,  2.98559219e-02, -7.81292561e-03,  3.25064927e-01,  1.35805145e-01, -9.71559901e-04, -2.76646502e-02, -5.77375516e-02,  9.55378935e-02, -2.37448722e-01,  4.22700606e-02,  2.76380867e-01,  1.11703485e-01,  8.88677016e-02,  5.32916896e-02, -1.48221165e-01, -3.52009125e-02,  2.03620985e-01, -1.81518987e-01,  9.79165137e-02,  4.06023413e-02, -1.80353791e-01, -4.12233025e-02, -1.40311718e-01,  1.31120443e-01,  9.09137130e-02, -1.44902498e-01, -2.05126241e-01,  2.10672930e-01, -1.24268889e-01, -9.40705463e-02,  1.44891188e-01, -1.19847670e-01, -1.74283370e-01, -2.00854555e-01,  5.20775318e-02, 3.74166280e-01,  7.90203363e-02, -1.52636811e-01, -9.50582884e-03, -2.45843865e-02, -2.99232546e-02,  5.54503640e-06,  5.70928007e-02, -8.09017271e-02, -1.12087876e-01, -1.24455154e-01,  9.77732986e-02, 1.61556095e-01,  5.14561590e-03, -1.09111689e-01,  1.24552011e-01, -1.05852447e-02,  7.00710118e-02,  2.64424980e-02,  2.65720766e-02, -7.94812664e-02, -1.01167057e-02, -1.54548258e-01, -1.49627328e-02, -4.85987030e-02, -1.25451282e-01, -7.83419907e-02,  9.57178175e-02, -3.92266437e-02,  2.00593114e-01,  3.73823866e-02,  2.36137398e-03, -1.20103545e-01,  5.55548482e-02, -1.60481781e-01,  4.78392579e-02, 1.84623227e-01, -3.36283416e-01,  2.87154794e-01,  1.63769260e-01, 3.24345306e-02,  9.96400341e-02,  5.34585752e-02,  6.37769774e-02, 8.40895157e-03, -1.00816466e-01, -2.00247690e-01, -1.03377171e-01, 1.53689049e-02,  4.24168147e-02,  3.22866775e-02,  5.63573558e-04,]),'BjookieMonster'],
                            ['Khell',np.array([-0.17167667, 0.09206803, 0.10366771, -0.03049685, -0.13605699, -0.09322222, -0.07623162, -0.05420944, 0.16111821, -0.03014767, 0.20660177, 0.03072538, -0.16635494, -0.06959266, -0.04864787, 0.12348884, -0.17318347, -0.10311881, 0.02477111, -0.03887189, 0.01302095, 0.0328631, -0.01728431, 0.03905208, -0.118238, -0.29955739, -0.10751943, -0.08221173, 0.00753316, -0.1067176, -0.00898117, 0.10291661, -0.11013805, -0.05193019, 0.0024103, 0.12255407, -0.09182015, -0.00554042, 0.17753433, 0.00737534, -0.14188306, 0.00445754, -0.00225968, 0.31637409, 0.19065703, 0.05070755, -0.02123814, -0.09287698, 0.21801956, -0.25692412, 0.04923129, 0.17553732, 0.15505323, 0.04002956, 0.1150623, -0.07639506, 0.07877546, 0.11596275, -0.26457465, 0.02570585, 0.04419234, -0.07257415, -0.03149741, -0.11101718, 0.1489429, 0.15614599, -0.0916468, -0.07934156, 0.13528143, -0.15634854, -0.12632419, 0.07872392, -0.07407676, -0.20246017, -0.34951603, -0.02086291, 0.33152911, 0.19298542, -0.2044315, -0.00663473, 0.0209441, -0.02470889, 0.10663309, 0.04167065, -0.17188063, -0.02404843, -0.15042977, -0.02134479, 0.13628462, 0.02113348, -0.03792093, 0.15277724, 0.07562415, 0.13426332, 0.03925346, 0.04478924, -0.07024017, -0.02278443, -0.16648944, -0.015773, 0.03488861, -0.03130141, -0.02232888, 0.09411849, -0.11646559, 0.21228094, 0.04445402, 0.02529586, -0.08790694, -0.02964385, -0.10559306, 0.04402736, 0.13356735, -0.2252596, 0.18394807, 0.10650516, -0.04879867, 0.13986161, 0.06685949, 0.00532956, -0.14779092, -0.11174309, -0.12751879, -0.0771023, 0.07706293, -0.06287712, 0.09938022, 0.0337316]),'Velocipastor'],
                            ['Sol',np.array([-0.06508087, 0.10704409, 0.03953771, -0.12145507, -0.12644212, 0.00874794, -0.09023664, -0.04626083, 0.21009958, -0.24569654, 0.09744484, -0.05188389, -0.22333486, 0.03257897, 0.0135618, 0.17535661, -0.19129428, -0.21873078, -0.04967026, -0.10278521, 0.07210241, 0.08242159, 0.00660577, 0.11527517, -0.20686093, -0.33984935, -0.07121621, -0.05304551, -0.02483523, -0.16560256, 0.07205684, 0.05984902, -0.14568369, 0.10339903, 0.00320311, 0.09308685, -0.03257393, -0.15983766, 0.25879848, 0.06366196, -0.24849802, -0.03680001, 0.06563561, 0.26062036, 0.22767489, -0.03538581, 0.03800561, -0.07083631, 0.23924734, -0.31017026, 0.06071727, 0.16538018, 0.05936825, 0.06159557, 0.137594, -0.13846816, 0.02305975, 0.16302839, -0.16863804, 0.08613089, 0.02483524, -0.12318623, 0.00511291, -0.04500373, 0.27863839, 0.07917735, -0.14391871, -0.16973367, 0.26610777, -0.16896755, -0.12234768, 0.14298499, -0.11410439, -0.15168421, -0.29237175, -0.0004172, 0.37397107, 0.13357617, -0.12886193, 0.08105619, -0.03351285, -0.03115841, -0.02542013, 0.23538722, -0.0483522, -0.07588843, -0.06944876, 0.05950505, 0.29603907, 0.01815441, -0.07704161, 0.26336721, 0.03870481, 0.0059769, 0.002683, 0.04464298, -0.16210316, -0.07363626, -0.08578022, -0.04818241, 0.02629539, -0.03416177, -0.08254968, 0.21401754, -0.20515159, 0.21274403, -0.08924203, -0.0627057, -0.04535527, 0.06446584, -0.09443327, -0.02650215, 0.11350284, -0.29381025, 0.09887333, 0.13954152, 0.06553463, 0.14017414, 0.02138437, 0.09948319, 0.05153609, -0.03929162, -0.19770123, -0.10408355, 0.03095459, 0.00078131, 0.00445925, 0.06303989]),'DragonSimp'],
                            ['Hedyn',np.array([-0.10490465, 0.1438034, 0.04340521, -0.05921197, -0.07439635, 0.03531232, -0.03255841, -0.02996691, 0.17971265, -0.03911512, 0.27151924, -0.01419582, -0.25926295, -0.0599971, -0.10249353, 0.15462479, -0.14650437, -0.11095367, -0.03072467, -0.05169189, -0.00100925, 0.04619905, -0.00450034, 0.04940035, -0.11242674, -0.34150949, 0.05936275, -0.0561754, 0.03298505, -0.14982715, -0.06740519, 0.16143945, -0.17578751, -0.02927932, 0.06098071, 0.14784065, -0.03586345, -0.04984989, 0.18332933, 0.03746532, -0.13726106, 0.02906479, 0.00685428, 0.34083787, 0.10536868, -0.01402119, 0.04772639, -0.1734632, 0.19653386, -0.24610333, 0.0989805, 0.19308922, 0.11655714, 0.0388988, 0.01360785, -0.12789975, -0.0308389, 0.14285156, -0.15351513, 0.0818615, 0.11433157, 0.01454011, -0.04482698, -0.1695146, 0.12724172, 0.04157625, -0.14285415, -0.10338241, 0.11223936, -0.08238945, -0.0601881, 0.05682018, -0.08963006, -0.23962194, -0.2367578, 0.13609967, 0.27439037, 0.1982026, -0.14192379, 0.00671128, -0.06426875, -0.04013504, 0.0114034, 0.06807864, -0.11575133, -0.0088718, -0.05373133, 0.04926247, 0.24154645, 0.02225758, -0.02188811, 0.22667433, 0.01437888, 0.01037977, -0.04743507, 0.04501811, -0.11678366, 0.04449376, -0.16879553, -0.0149247, 0.00370525, -0.11575621, -0.00809265, 0.12036442, -0.24429516, 0.1220841, -0.0178813, 0.00547687, 0.09195269, 0.02298281, -0.11328493, -0.08206152, 0.12885006, -0.23511188, 0.19304903, 0.17204112, 0.21671958, 0.13578936, 0.14508626, 0.03093109, 0.08424962, -0.06922384, -0.12096157, -0.08768222, 0.12220036, 0.00036435, -0.01679565, 0.0030117]),'CanIGetAHand'],
                            ['Roan',np.array([-0.18170246, 0.05271934, 0.07385418, -0.08230815, -0.16250981, 0.04770295, -0.09353397, 0.03303054, 0.11875495, -0.11202836, 0.23585258, -0.06186866, -0.27403474, 0.0253159, -0.05906642, 0.15831046, -0.11648206, -0.11904437, -0.03529483, -0.10262959, -0.06619179, 0.10165762, -0.06666309, 0.08711397, -0.08818322, -0.29679027, -0.04091524, -0.08034791, 0.01276306, -0.13879378, -0.07512917, 0.09595, -0.15816346, -0.04682378, 0.07196216, 0.13416925, -0.04246683, -0.11009005, 0.14046419, 0.03705064, -0.08422215, -0.0750146, 0.08133022, 0.30722618, 0.08457159, 0.06322689, 0.00683346, -0.04943656, 0.10674896, -0.24281327, 0.092017, 0.15237488, 0.12090179, 0.04023578, 0.08857723, -0.13073605, 0.04742688, 0.14417985, -0.11700613, 0.06664424, 0.05973235, -0.00470983, -0.00705414, -0.08468676, 0.22524627, 0.08620545, -0.04853966, -0.15698014, 0.18959686, -0.09584125, -0.11815379, 0.10857389, -0.09895754, -0.15413448, -0.18615451, 0.06426574, 0.32519782, 0.19981723, -0.10912441, 0.04307393, -0.01700494, -0.10110063, 0.03705372, 0.03929001, -0.08814143, -0.06415376, -0.08671787, 0.05121798, 0.26764578, 0.03917938, -0.00491704, 0.14457744, 0.03946414, -0.06067492, 0.03603533, -0.00549771, -0.0895345, -0.01794496, -0.11740087, -0.07887301, 0.07015894, -0.04527388, -0.04052237, 0.1369165, -0.21225302, 0.08191926, -0.04245991, -0.072399, -0.00868035, 0.01541813, -0.11117078, -0.00097357, 0.15331231, -0.22664967, 0.11732004, 0.11519699, 0.1022245, 0.11048344, 0.08615539, 0.02888647, 0.05352353, -0.09943299, -0.15137649, -0.16606732, 0.09795673, -0.02668438, 0.04565628, 0.0346655]),'SongOfOak'],
                            ['Christine',np.array([-0.06239505, 0.13190003, 0.03639989, -0.09070025, -0.1808361, 0.04264699, 0.03981895, -0.14343068, 0.2212307, -0.08604459, 0.23492855, 0.02546377, -0.21816958, -0.02258407, -0.03593722, 0.14834039, -0.15094778, -0.18234141, -0.05330178, -0.08728112, 0.0173263, 0.01850059, -0.01825078, 0.0629814, -0.11371233, -0.24260339, -0.02308544, -0.01160223, 0.08243669, -0.09083511, 0.01399625, 0.14609635, -0.15493698, 0.02559846, 0.02449545, 0.02499655, -0.10316277, -0.16083939, 0.17270276, -0.12328103, -0.2246598, -0.02247352, 0.0791156, 0.2306767, 0.26069298, -0.09497719, 0.03276353, -0.13918211, 0.11598954, -0.29121792, 0.06353832, 0.16100326, -0.08325487, 0.05535791, 0.03983378, -0.19411926, -0.08762433, 0.14270176, -0.17912309, 0.01289275, 0.06329431, -0.12558375, -0.09186192, -0.21002352, 0.14817163, 0.18132921, -0.09640856, -0.31051132, 0.18042201, -0.23705038, -0.10556415, 0.12647159, -0.13159451, -0.18234393, -0.26627183, 0.04092537, 0.3299121, 0.21568356, -0.0645036, 0.10754474, -0.02680555, 0.01640744, 0.04534103, 0.11457534, 0.02916364, -0.07073542, -0.10488642, 0.03447268, 0.21916813, -0.03907005, -0.08734191, 0.25482923, -0.00625652, -0.08776585, -0.01658187, 0.10708617, -0.09131677, 0.05625641, -0.17592975, -0.03873466, 0.00932152, 0.0142299, 0.03639187, 0.18753049, -0.11041179, 0.1879824, -0.06597289, 0.08981457, 0.00706134, -0.12159836, -0.02171038, -0.00526678, 0.12119575, -0.26311633, 0.20639424, 0.05651565, 0.11770799, 0.15130918, 0.04367356, 0.07822885, 0.05094284, -0.08590095, -0.17918491, -0.00391553, 0.0353566, -0.04408484, 0.01641661, 0.0713986]),'CollosalNerd'],
                            ]

    return known_image_encodings
