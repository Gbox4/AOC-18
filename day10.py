from time import sleep

print("start")

if True:
    puzzle = """position=< -9767,  50146> velocity=< 1, -5>
    position=< 20243,  20134> velocity=<-2, -2>
    position=< -9771,  50141> velocity=< 1, -5>
    position=< 20206, -49884> velocity=<-2,  5>
    position=< 30233,  40142> velocity=<-3, -4>
    position=<-29829,  30132> velocity=< 3, -3>
    position=<-39787, -19879> velocity=< 4,  2>
    position=< 40188,  30138> velocity=<-4, -3>
    position=<-19811, -49890> velocity=< 2,  5>
    position=< -9771, -19880> velocity=< 1,  2>
    position=< 30188, -39880> velocity=<-3,  4>
    position=<-29788, -29882> velocity=< 3,  3>
    position=<-19790, -39886> velocity=< 2,  4>
    position=< 10179, -39881> velocity=<-1,  4>
    position=< 10211,  -9871> velocity=<-1,  1>
    position=< 30238,  20137> velocity=<-3, -2>
    position=< 50239, -19878> velocity=<-5,  2>
    position=< 40204,  30135> velocity=<-4, -3>
    position=< 40225,  40139> velocity=<-4, -4>
    position=< 40231,  50143> velocity=<-4, -5>
    position=<-19793,  40141> velocity=< 2, -4>
    position=< 50247,  50146> velocity=<-5, -5>
    position=< 50203,  20129> velocity=<-5, -2>
    position=< 10238,  10132> velocity=<-1, -1>
    position=< 30217, -39888> velocity=<-3,  4>
    position=< 50193,  30132> velocity=<-5, -3>
    position=<-49803, -39881> velocity=< 5,  4>
    position=<-29820, -29877> velocity=< 3,  3>
    position=< 30238,  20138> velocity=<-3, -2>
    position=< 20207,  10126> velocity=<-2, -1>
    position=<-39803,  40136> velocity=< 4, -4>
    position=< 50248, -39888> velocity=<-5,  4>
    position=<-19801, -29884> velocity=< 2,  3>
    position=< 40244,  -9876> velocity=<-4,  1>
    position=<-49799,  50145> velocity=< 5, -5>
    position=<-19806,  50140> velocity=< 2, -5>
    position=< 20223,  20134> velocity=<-2, -2>
    position=<-29813, -49891> velocity=< 3,  5>
    position=<-29809, -49883> velocity=< 3,  5>
    position=< -9819,  30141> velocity=< 1, -3>
    position=< 40220,  10130> velocity=<-4, -1>
    position=< -9771,  10131> velocity=< 1, -1>
    position=< 50192, -49883> velocity=<-5,  5>
    position=< 30244, -19877> velocity=<-3,  2>
    position=< 50247,  50143> velocity=<-5, -5>
    position=< 10240,  50138> velocity=<-1, -5>
    position=<-49830, -19874> velocity=< 5,  2>
    position=<-19780,  20129> velocity=< 2, -2>
    position=< 40241,  50147> velocity=<-4, -5>
    position=< 50217, -29882> velocity=<-5,  3>
    position=< 40228,  40141> velocity=<-4, -4>
    position=<-39804,  50141> velocity=< 4, -5>
    position=< 40198, -49887> velocity=<-4,  5>
    position=< -9803, -49886> velocity=< 1,  5>
    position=<-19817, -49890> velocity=< 2,  5>
    position=<-49835,  10135> velocity=< 5, -1>
    position=< 10219,  50146> velocity=<-1, -5>
    position=< 40188, -39884> velocity=<-4,  4>
    position=<-29832,  -9880> velocity=< 3,  1>
    position=< 40201,  40136> velocity=<-4, -4>
    position=<-49791,  20129> velocity=< 5, -2>
    position=< 20222,  30134> velocity=<-2, -3>
    position=< 20207,  30132> velocity=<-2, -3>
    position=<-29817, -19880> velocity=< 3,  2>
    position=< 20206, -29881> velocity=<-2,  3>
    position=<-29833,  10127> velocity=< 3, -1>
    position=< 40249,  30136> velocity=<-4, -3>
    position=<-19820,  30137> velocity=< 2, -3>
    position=< 30237,  -9873> velocity=<-3,  1>
    position=< 20217, -39884> velocity=<-2,  4>
    position=< 50191,  10130> velocity=<-5, -1>
    position=<-29825,  50146> velocity=< 3, -5>
    position=< 10192,  10135> velocity=<-1, -1>
    position=< 50191,  10130> velocity=<-5, -1>
    position=< 50223,  20129> velocity=<-5, -2>
    position=< 20238,  40138> velocity=<-2, -4>
    position=< 30221,  -9872> velocity=<-3,  1>
    position=<-49803, -39881> velocity=< 5,  4>
    position=<-39836, -39887> velocity=< 4,  4>
    position=<-29820, -29885> velocity=< 3,  3>
    position=<-29806,  -9876> velocity=< 3,  1>
    position=<-29791, -19883> velocity=< 3,  2>
    position=<-49835,  50147> velocity=< 5, -5>
    position=<-39825, -19874> velocity=< 4,  2>
    position=<-49806, -39887> velocity=< 5,  4>
    position=< -9766,  10134> velocity=< 1, -1>
    position=<-19819, -49892> velocity=< 2,  5>
    position=<-49778,  10135> velocity=< 5, -1>
    position=< 20231, -29886> velocity=<-2,  3>
    position=< -9817, -19883> velocity=< 1,  2>
    position=< -9778,  20133> velocity=< 1, -2>
    position=< 50220, -19881> velocity=<-5,  2>
    position=< 10211,  40144> velocity=<-1, -4>
    position=<-39783,  30133> velocity=< 4, -3>
    position=<-19769,  40135> velocity=< 2, -4>
    position=<-39791,  30135> velocity=< 4, -3>
    position=<-19814, -49888> velocity=< 2,  5>
    position=<-49829, -49883> velocity=< 5,  5>
    position=<-19790,  -9872> velocity=< 2,  1>
    position=< 40216, -49892> velocity=<-4,  5>
    position=< 20238, -39882> velocity=<-2,  4>
    position=< 10235,  50138> velocity=<-1, -5>
    position=<-19814, -29878> velocity=< 2,  3>
    position=< 30217,  10129> velocity=<-3, -1>
    position=< 10235,  30133> velocity=<-1, -3>
    position=< 10188,  40144> velocity=<-1, -4>
    position=< 10235, -19874> velocity=<-1,  2>
    position=<-19793,  30135> velocity=< 2, -3>
    position=< 20198,  30141> velocity=<-2, -3>
    position=<-39815,  40135> velocity=< 4, -4>
    position=< 50252,  40138> velocity=<-5, -4>
    position=< 30222, -19880> velocity=<-3,  2>
    position=< 20190, -19883> velocity=<-2,  2>
    position=< 10216, -29878> velocity=<-1,  3>
    position=< 20187, -39888> velocity=<-2,  4>
    position=< 10179,  40143> velocity=<-1, -4>
    position=< 20203, -29886> velocity=<-2,  3>
    position=< 40188,  50143> velocity=<-4, -5>
    position=< 50228, -29885> velocity=<-5,  3>
    position=< 10237,  -9877> velocity=<-1,  1>
    position=<-49804, -19877> velocity=< 5,  2>
    position=<-29793, -49888> velocity=< 3,  5>
    position=< 20235,  30140> velocity=<-2, -3>
    position=<-39788,  10133> velocity=< 4, -1>
    position=<-19793,  10132> velocity=< 2, -1>
    position=< 30201,  40143> velocity=<-3, -4>
    position=< 40212,  50138> velocity=<-4, -5>
    position=<-19786,  -9875> velocity=< 2,  1>
    position=< -9810, -19879> velocity=< 1,  2>
    position=< 30219, -49888> velocity=<-3,  5>
    position=< 50218, -49892> velocity=<-5,  5>
    position=< 40225, -29883> velocity=<-4,  3>
    position=< 30233,  30136> velocity=<-3, -3>
    position=< 10211, -19881> velocity=<-1,  2>
    position=< 10216,  -9878> velocity=<-1,  1>
    position=<-19794,  20136> velocity=< 2, -2>
    position=< 10188,  40141> velocity=<-1, -4>
    position=< -9819,  50145> velocity=< 1, -5>
    position=< -9774,  -9877> velocity=< 1,  1>
    position=< 10227, -39883> velocity=<-1,  4>
    position=< -9816,  40139> velocity=< 1, -4>
    position=<-39775,  10133> velocity=< 4, -1>
    position=< -9778,  -9880> velocity=< 1,  1>
    position=< 10228,  20129> velocity=<-1, -2>
    position=< 20207,  30136> velocity=<-2, -3>
    position=< 10188, -39883> velocity=<-1,  4>
    position=< 30209, -39888> velocity=<-3,  4>
    position=<-39826, -19874> velocity=< 4,  2>
    position=<-19790,  20135> velocity=< 2, -2>
    position=<-39775, -49889> velocity=< 4,  5>
    position=<-19771,  50143> velocity=< 2, -5>
    position=< 20238,  20131> velocity=<-2, -2>
    position=< 40249, -49885> velocity=<-4,  5>
    position=< 50235,  10127> velocity=<-5, -1>
    position=<-19806,  20138> velocity=< 2, -2>
    position=<-19789, -19882> velocity=< 2,  2>
    position=< 30237,  20135> velocity=<-3, -2>
    position=< 10230, -49887> velocity=<-1,  5>
    position=<-29825, -39880> velocity=< 3,  4>
    position=< 50219,  30132> velocity=<-5, -3>
    position=< 40244, -39885> velocity=<-4,  4>
    position=< -9811, -39888> velocity=< 1,  4>
    position=< 50228,  10127> velocity=<-5, -1>
    position=< 10231,  -9880> velocity=<-1,  1>
    position=< 10232,  20131> velocity=<-1, -2>
    position=< 40232,  40136> velocity=<-4, -4>
    position=< 20214,  20136> velocity=<-2, -2>
    position=< -9811, -49885> velocity=< 1,  5>
    position=< 50207,  20135> velocity=<-5, -2>
    position=<-49799, -39884> velocity=< 5,  4>
    position=<-39820,  30137> velocity=< 4, -3>
    position=< 40236, -19882> velocity=<-4,  2>
    position=< 20243, -39884> velocity=<-2,  4>
    position=< 40236, -19875> velocity=<-4,  2>
    position=< 40197, -29880> velocity=<-4,  3>
    position=<-49787, -29879> velocity=< 5,  3>
    position=<-49794,  10129> velocity=< 5, -1>
    position=<-29804,  20132> velocity=< 3, -2>
    position=<-29824, -49892> velocity=< 3,  5>
    position=<-19785, -29879> velocity=< 2,  3>
    position=< 40236,  40144> velocity=<-4, -4>
    position=<-19830,  10131> velocity=< 2, -1>
    position=<-39785,  30132> velocity=< 4, -3>
    position=< -9816,  30141> velocity=< 1, -3>
    position=< 10197,  50141> velocity=<-1, -5>
    position=< 20198, -49883> velocity=<-2,  5>
    position=< 30217,  50146> velocity=<-3, -5>
    position=<-39799,  40140> velocity=< 4, -4>
    position=<-19774, -49885> velocity=< 2,  5>
    position=< 30212,  -9880> velocity=<-3,  1>
    position=<-19772,  -9876> velocity=< 2,  1>
    position=< 50228,  10126> velocity=<-5, -1>
    position=< -9790, -29878> velocity=< 1,  3>
    position=<-19826, -49892> velocity=< 2,  5>
    position=< -9771, -39888> velocity=< 1,  4>
    position=<-19795, -49887> velocity=< 2,  5>
    position=<-19793,  -9880> velocity=< 2,  1>
    position=<-19801,  40137> velocity=< 2, -4>
    position=<-39812,  50145> velocity=< 4, -5>
    position=< 50239,  -9876> velocity=<-5,  1>
    position=<-29833, -29880> velocity=< 3,  3>
    position=< 50210,  40142> velocity=<-5, -4>
    position=< 40220,  20130> velocity=<-4, -2>
    position=<-29809, -49888> velocity=< 3,  5>
    position=< 40193, -19875> velocity=<-4,  2>
    position=< -9803,  50143> velocity=< 1, -5>
    position=< 30230, -49890> velocity=<-3,  5>
    position=< 10187,  20138> velocity=<-1, -2>
    position=< 40244,  40144> velocity=<-4, -4>
    position=< 30212, -39885> velocity=<-3,  4>
    position=<-49823,  30134> velocity=< 5, -3>
    position=< 40199,  40135> velocity=<-4, -4>
    position=< 20230,  10128> velocity=<-2, -1>
    position=< 10211,  20132> velocity=<-1, -2>
    position=< 40231,  30137> velocity=<-4, -3>
    position=< 30185,  20135> velocity=<-3, -2>
    position=< 30217,  40137> velocity=<-3, -4>
    position=< 20194, -19883> velocity=<-2,  2>
    position=< 10216,  30141> velocity=<-1, -3>
    position=<-39820,  40137> velocity=< 4, -4>
    position=<-39794,  10131> velocity=< 4, -1>
    position=< 50239,  30134> velocity=<-5, -3>
    position=<-39828, -49892> velocity=< 4,  5>
    position=< 20224, -29881> velocity=<-2,  3>
    position=<-49802,  10128> velocity=< 5, -1>
    position=< 40196,  30140> velocity=<-4, -3>
    position=<-49837,  40144> velocity=< 5, -4>
    position=<-19777,  30135> velocity=< 2, -3>
    position=< 50233,  40140> velocity=<-5, -4>
    position=< 30227,  40135> velocity=<-3, -4>
    position=< 30226,  10127> velocity=<-3, -1>
    position=< 30246, -29881> velocity=<-3,  3>
    position=< 30209,  50138> velocity=<-3, -5>
    position=< -9827,  -9879> velocity=< 1,  1>
    position=< 10235,  40136> velocity=<-1, -4>
    position=<-19785,  -9871> velocity=< 2,  1>
    position=<-49815, -49889> velocity=< 5,  5>
    position=<-49839, -29885> velocity=< 5,  3>
    position=<-19795,  50143> velocity=< 2, -5>
    position=< 50231,  -9873> velocity=<-5,  1>
    position=<-19786, -49891> velocity=< 2,  5>
    position=< 30186, -29877> velocity=<-3,  3>
    position=<-19813,  10130> velocity=< 2, -1>
    position=<-49788,  30136> velocity=< 5, -3>
    position=< 10203, -19881> velocity=<-1,  2>
    position=< 20198,  -9876> velocity=<-2,  1>
    position=<-39783,  40137> velocity=< 4, -4>
    position=<-39804, -19876> velocity=< 4,  2>
    position=<-39784,  -9880> velocity=< 4,  1>
    position=<-39817,  20131> velocity=< 4, -2>
    position=< 40196,  30132> velocity=<-4, -3>
    position=< 30242,  -9879> velocity=<-3,  1>
    position=<-39786,  50142> velocity=< 4, -5>
    position=<-29833,  -9876> velocity=< 3,  1>
    position=< 40200,  40138> velocity=<-4, -4>
    position=< 10211, -49885> velocity=<-1,  5>
    position=< 20222, -49888> velocity=<-2,  5>
    position=< 50239,  10134> velocity=<-5, -1>
    position=<-49794,  50145> velocity=< 5, -5>
    position=<-39833, -49892> velocity=< 4,  5>
    position=< 50223, -29885> velocity=<-5,  3>
    position=<-29796, -39888> velocity=< 3,  4>
    position=<-29793,  10135> velocity=< 3, -1>
    position=< 30211, -29886> velocity=<-3,  3>
    position=<-29772, -29883> velocity=< 3,  3>
    position=< -9818,  -9880> velocity=< 1,  1>
    position=< 40236,  30139> velocity=<-4, -3>
    position=< 40240,  50144> velocity=<-4, -5>
    position=< 50226,  10132> velocity=<-5, -1>
    position=<-29815,  20135> velocity=< 3, -2>
    position=< 40217, -19882> velocity=<-4,  2>
    position=<-39812,  20138> velocity=< 4, -2>
    position=< -9817,  40140> velocity=< 1, -4>
    position=<-39808,  20129> velocity=< 4, -2>
    position=< 50212,  30141> velocity=<-5, -3>
    position=< 20243,  50144> velocity=<-2, -5>
    position=< -9787,  10133> velocity=< 1, -1>
    position=< 30209,  50144> velocity=<-3, -5>
    position=<-49815, -39884> velocity=< 5,  4>
    position=<-29820, -29886> velocity=< 3,  3>
    position=< 20182,  40142> velocity=<-2, -4>
    position=< 10235,  20135> velocity=<-1, -2>
    position=< 10179,  30135> velocity=<-1, -3>
    position=<-29792,  20130> velocity=< 3, -2>
    position=<-39820, -19881> velocity=< 4,  2>
    position=<-19794, -39882> velocity=< 2,  4>
    position=<-19796, -29883> velocity=< 2,  3>
    position=< 10231,  30136> velocity=<-1, -3>
    position=< -9779,  30141> velocity=< 1, -3>
    position=< -9771,  30140> velocity=< 1, -3>
    position=< -9779,  -9880> velocity=< 1,  1>
    position=< 50207, -19883> velocity=<-5,  2>
    position=< 40204,  30132> velocity=<-4, -3>
    position=<-19806, -49888> velocity=< 2,  5>
    position=<-39784,  40142> velocity=< 4, -4>
    position=<-19769,  30136> velocity=< 2, -3>
    position=< 30236,  -9880> velocity=<-3,  1>
    position=<-49794,  20138> velocity=< 5, -2>
    position=<-49826,  30141> velocity=< 5, -3>
    position=<-19769, -49886> velocity=< 2,  5>
    position=< 20201,  20131> velocity=<-2, -2>
    position=<-19798,  30137> velocity=< 2, -3>
    position=<-19774,  40140> velocity=< 2, -4>
    position=<-39824,  40135> velocity=< 4, -4>
    position=<-49794, -19878> velocity=< 5,  2>
    position=<-49815,  -9877> velocity=< 5,  1>
    position=< -9784,  -9880> velocity=< 1,  1>
    position=<-19769,  -9878> velocity=< 2,  1>
    position=<-29831, -29886> velocity=< 3,  3>
    position=< 30217,  40135> velocity=<-3, -4>
    position=< 40244, -49885> velocity=<-4,  5>
    position=<-19785,  50145> velocity=< 2, -5>
    position=< 50191, -39881> velocity=<-5,  4>
    position=<-39796,  30138> velocity=< 4, -3>
    position=< 10205,  -9880> velocity=<-1,  1>
    position=<-49806,  40136> velocity=< 5, -4>
    position=< 10231,  10132> velocity=<-1, -1>
    position=< 20194, -29877> velocity=<-2,  3>
    position=<-49786,  20132> velocity=< 5, -2>
    position=< 50228,  20133> velocity=<-5, -2>
    position=<-49794, -49890> velocity=< 5,  5>
    position=< 30209,  40142> velocity=<-3, -4>
    position=< 20219, -29877> velocity=<-2,  3>
    position=<-29780,  20130> velocity=< 3, -2>
    position=<-29831, -19883> velocity=< 3,  2>
    position=<-29817, -39889> velocity=< 3,  4>
    position=<-39785,  30137> velocity=< 4, -3>
    position=<-49838, -49892> velocity=< 5,  5>
    position=< 50204, -29884> velocity=<-5,  3>
    position=< 50234,  50138> velocity=<-5, -5>
    position=<-49815,  40142> velocity=< 5, -4>
    position=< 40216,  30136> velocity=<-4, -3>
    position=<-19769, -19883> velocity=< 2,  2>
    position=<-29798,  30138> velocity=< 3, -3>
    position=< -9782,  30140> velocity=< 1, -3>
    position=<-49810, -49889> velocity=< 5,  5>
    position=<-19805, -29886> velocity=< 2,  3>
    position=< 50240, -19879> velocity=<-5,  2>
    position=<-39776,  -9873> velocity=< 4,  1>
    position=<-19813,  50143> velocity=< 2, -5>
    position=<-49786, -29884> velocity=< 5,  3>
    position=< 40233, -49883> velocity=<-4,  5>
    position=<-39785,  -9880> velocity=< 4,  1>
    position=<-19810,  50146> velocity=< 2, -5>
    position=< -9803, -29885> velocity=< 1,  3>
    position=<-19793,  40142> velocity=< 2, -4>
    position=< 20230, -39880> velocity=<-2,  4>
    position=<-49807, -19877> velocity=< 5,  2>
    position=<-49822, -19878> velocity=< 5,  2>
    position=<-49791,  50141> velocity=< 5, -5>
    position=< 30226, -19878> velocity=<-3,  2>
    position=< 30222, -49885> velocity=<-3,  5>
    position=< 30229,  50143> velocity=<-3, -5>
    position=< -9782,  50141> velocity=< 1, -5>
    position=< -9795, -19883> velocity=< 1,  2>
    position=< 40190, -29877> velocity=<-4,  3>
    position=< 10179,  30134> velocity=<-1, -3>
    position=<-49823,  -9874> velocity=< 5,  1>
    position=<-29799,  40139> velocity=< 3, -4>
    position=<-39776, -39882> velocity=< 4,  4>
    position=<-19782,  50144> velocity=< 2, -5>
    position=< -9811,  -9876> velocity=< 1,  1>
    position=< 20219, -29877> velocity=<-2,  3>
    position=<-49779,  20137> velocity=< 5, -2>
    position=< -9779,  10134> velocity=< 1, -1>
    position=< 20201, -49885> velocity=<-2,  5>
    position=<-39832,  20138> velocity=< 4, -2>
    position=< 20243,  50139> velocity=<-2, -5>
    position=<-39780,  50144> velocity=< 4, -5>
    position=< 20215, -39887> velocity=<-2,  4>
    position=<-39788, -49892> velocity=< 4,  5>
    position=<-29776,  50140> velocity=< 3, -5>
    position=< 40220, -49887> velocity=<-4,  5>
    position=<-19820,  40135> velocity=< 2, -4>
    position=< 50200,  -9871> velocity=<-5,  1>
    position=<-49836, -39880> velocity=< 5,  4>
    position=< 50236, -19875> velocity=<-5,  2>
    position=< 50228, -29884> velocity=<-5,  3>
    position=< 30230, -39883> velocity=<-3,  4>"""

class Point:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv

def printBoard(code, length, xmin, ymin):
    length += 5
    board = []
    for y in range(length):
        newRow = []
        for x in range(length):
            newRow.append(".")
        board.append(newRow)
    
    for p in code:
        #its minus because the xmin is positive
        boardposy = p.y-ymin
        boardposx = p.x-xmin
        if not (boardposy >= length or boardposx >= length):
            board[boardposy][boardposx] = "#"

    for y in range(len(board)):
        prtrow = ""
        for x in range(len(board[y])):
            prtrow = prtrow + board[y][x]
        
        print(prtrow)

def parse(code):
    code = code.split("\n")
    new = []
    

    for i in code:

        x = 0
        y = 0
        xv = 0
        yv = 0

        parts = i.split("position=<")

        parts = parts[1].split("> velocity=<")

        posCoords = parts[0].split(",")

        x = posCoords[0]
        y = posCoords[1]

        velCoords = parts[1].split(",")
        xv = velCoords[0]
        yv = velCoords[1]

        yv = yv [:len(yv)-1]

        new.append(Point(int(x),int(y),int(xv),int(yv)))

    return new

def twoPoints(p1,p2):
    if p1.x == p2.x and p1.y == p2.y:
        return True

    else:
        return False


code = parse(puzzle)


xmax = 0
xmin = 0
ymax = 0
ymin = 0

for p in code:
    if p.x > xmax:
        xmax = p.x
    if p.y > ymax:
        ymax = p.y
    
    if p.x < xmin:
        xmin = p.x
    if p.y < ymin:
        ymin = p.y



loopn = 0
loopminx = 0
loopmaxx = 0
loopminy = 0
loopmaxy = 0
lastxdist = 9999999
lastydist = 9999999

passedmindist = False

while True:

    loopn += 1

    loopminx = (xmin+xmax)/2
    loopmaxx = (xmin+xmax)/2
    loopminy = (xmin+xmax)/2
    loopmaxy = (xmin+xmax)/2

    for p in code:
        #finding largest and smallest on x axis

        p.x += p.xv
        p.y -= p.yv

        if p.x < loopminx:
            loopminx = p.x
        
        if p.x > loopmaxx:
            loopmaxx = p.x
        
        if p.y < loopminy:
            loopminy = p.y
        
        if p.y > loopmaxy:
            loopmaxy = p.y
    
    xdist = abs(loopmaxx-loopminx)
    ydist = abs(loopmaxy-loopminy)
    

    #ALL CODE TO SEE IF THIS IS A GOOD OUTPUT GOES HERE
    

    if loopn <= 10003 and loopn >= 10000:
    #if xdist > lastxdist:
        br = ""
        for i in range(120):
            br = br+"-"
        print (br)
        printBoard(code, 100, loopminx, loopminy)
        #print("X distance: {0}".format(xdist), "Y distance: {0}".format(ydist), "Loop number: {0}".format(loopn))
        break

    lastxdist = xdist
    lastydist = ydist

