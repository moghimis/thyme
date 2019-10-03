from collections import namedtuple

import numpy
import pytest

from thyme.model.hycom import vertical_interpolation

VerticalValues = namedtuple(
    'VerticalValues',
    ['u',
     'v',
     'depth',
     'num_x',
     'num_y',
     'time_index',
     'target_depth_surface',
     'target_depth_default',
     'target_depth_deep',
     'expected_u_target_depth_default',
     'expected_v_target_depth_default',
     'expected_u_target_depth_surface',
     'expected_v_target_depth_surface',
     'expected_u_target_depth_deep',
     'expected_v_target_depth_deep'])


@pytest.fixture
def vertical_values():

    u = numpy.ma.array(
        data=[[[[-0.14429612457752228, -0.1557592898607254, -0.1639900505542755],
              [-0.13332930207252502, -0.13850903511047363, -0.14700627326965332]],

            [[-0.17176321148872375, -0.18649248778820038, -0.1963706910610199],
             [-0.10463598370552063, -0.11853943765163422, -0.12382897734642029]],

            [[-0.1860588788986206, -0.2024313062429428, -0.21306045353412628],
             [-0.11270792037248611, -0.1282253861427307, -0.13397538661956787]],

            [[-0.1959017515182495, -0.21337155997753143, -0.22445325553417206],
             [-0.11817137151956558, -0.13474631309509277, -0.14073477685451508]],

            [[-0.20371614396572113, -0.222026988863945, -0.23342110216617584],
             [-0.12233472615480423, -0.13967420160770416, -0.1458158940076828]],

            [[-0.21044501662254333, -0.22945916652679443, -0.2410876452922821],
             [-0.12573498487472534, -0.14364899694919586, -0.1499125063419342]],

            [[-0.21648438274860382, -0.23612338304519653, -0.2479390650987625],
             [-0.12864403426647186, -0.14699482917785645, -0.1533738672733307]],

            [[-0.22195807099342346, -0.2421712726354599, -0.2541458308696747],
             [-0.13121622800827026, -0.14990080893039703, -0.15639856457710266]],

            [[-0.22682039439678192, -0.24759206175804138, -0.2597068250179291],
             [-0.1335427612066269, -0.15248820185661316, -0.15910528600215912]],

            [[-0.23106896877288818, -0.2523146867752075, -0.2645571827888489],
             [-0.13567526638507843, -0.15483982861042023, -0.16156552731990814]],

            [[-0.2349419891834259, -0.25623324513435364, -0.26865893602371216],
             [-0.137639582157135, -0.15701685845851898, -0.16382475197315216]],

            [[-0.23808951675891876, -0.25947651267051697, -0.2720396816730499],
             [-0.13947321474552155, -0.15906816720962524, -0.16592034697532654]],

            [[-0.24045346677303314, -0.2621067762374878, -0.2748018801212311],
             [-0.14117150008678436, -0.1610313355922699, -0.16789506375789642]],

            [[-0.2426738142967224, -0.26430219411849976, -0.2770835757255554],
             [-0.14282099902629852, -0.16296876966953278, -0.16980309784412384]],

            [[-0.24465344846248627, -0.26616188883781433, -0.27903714776039124],
             [-0.14445151388645172, -0.16493166983127594, -0.17171379923820496]],

            [[-0.2462834268808365, -0.2679187059402466, -0.2808115780353546],
             [-0.14620362222194672, -0.16701747477054596, -0.17371375858783722]],

            [[-0.24794217944145203, -0.26969125866889954, -0.2825746238231659],
             [-0.14814794063568115, -0.1692989468574524, -0.17590203881263733]],

            [[-0.24987787008285522, -0.271731436252594, -0.28456488251686096],
             [-0.15038220584392548, -0.17185862362384796, -0.17835474014282227]],

            [[-0.25258249044418335, -0.27453669905662537, -0.28726720809936523],
             [-0.15316414833068848, -0.17494668066501617, -0.18129220604896545]],

            [[-0.25681057572364807, -0.2789645791053772, -0.29178279638290405],
             [-0.157413512468338, -0.17946366965770721, -0.18561050295829773]],

            [[-0.14429612457752228, -0.1557592898607254, -0.1639900505542755],
             [-0.13332930207252502, -0.13850903511047363, -0.14700627326965332]],

            [[-0.17176321148872375, -0.18649248778820038, -0.1963706910610199],
             [-0.10463598370552063, -0.11853943765163422, -0.12382897734642029]],

            [[-0.1860588788986206, -0.2024313062429428, -0.21306045353412628],
             [-0.11270792037248611, -0.1282253861427307, -0.13397538661956787]],

            [[-0.1959017515182495, -0.21337155997753143, -0.22445325553417206],
             [-0.11817137151956558, -0.13474631309509277, -0.14073477685451508]],

            [[-0.20371614396572113, -0.222026988863945, -0.23342110216617584],
             [-0.12233472615480423, -0.13967420160770416, -0.1458158940076828]],

            [[-0.21044501662254333, -0.22945916652679443, -0.2410876452922821],
             [-0.12573498487472534, -0.14364899694919586, -0.1499125063419342]],

            [[-0.21648438274860382, -0.23612338304519653, -0.2479390650987625],
             [-0.12864403426647186, -0.14699482917785645, -0.1533738672733307]],

            [[-0.22195807099342346, -0.2421712726354599, -0.2541458308696747],
             [-0.13121622800827026, -0.14990080893039703, -0.15639856457710266]],

            [[-0.22682039439678192, -0.24759206175804138, -0.2597068250179291],
             [-0.1335427612066269, -0.15248820185661316, -0.15910528600215912]],

            [[-0.23106896877288818, -0.2523146867752075, -0.2645571827888489],
             [-0.13567526638507843, -0.15483982861042023, -0.16156552731990814]],

            [[-0.2349419891834259, -0.25623324513435364, -0.26865893602371216],
             [-0.137639582157135, -0.15701685845851898, -0.16382475197315216]],

            [[-0.23808951675891876, -0.25947651267051697, -0.2720396816730499],
             [-0.13947321474552155, -0.15906816720962524, -0.16592034697532654]],

            [[-0.24045346677303314, -0.2621067762374878, -0.2748018801212311],
             [-0.14117150008678436, -0.1610313355922699, -0.16789506375789642]],

            [[-0.2426738142967224, -0.26430219411849976, -0.2770835757255554],
             [-0.14282099902629852, -0.16296876966953278, -0.16980309784412384]],

            [[-0.24465344846248627, -0.26616188883781433, -0.27903714776039124],
             [-0.14445151388645172, -0.16493166983127594, -0.17171379923820496]],

            [[-0.2462834268808365, -0.2679187059402466, -0.2808115780353546],
             [-0.14620362222194672, -0.16701747477054596, -0.17371375858783722]],

            [[-0.24794217944145203, -0.26969125866889954, -0.2825746238231659],
             [-0.14814794063568115, -0.1692989468574524, -0.17590203881263733]],

            [[-0.24987787008285522, -0.271731436252594, -0.28456488251686096],
             [-0.15038220584392548, -0.17185862362384796, -0.17835474014282227]],

            [[-0.25258249044418335, -0.27453669905662537, -0.28726720809936523],
             [-0.15316414833068848, -0.17494668066501617, -0.18129220604896545]],

            [[-0.25681057572364807, -0.2789645791053772, -0.29178279638290405],
             [-0.157413512468338, -0.17946366965770721, -0.18561050295829773]]]],

        mask=[[[[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                 [False, False, False]]]],
        fill_value=1.2676506e+30,
        dtype='float32'
    )

    v = numpy.ma.array(
        data=[[[[-0.015962883830070496, -0.014421091414988041, -0.015121867880225182],
                [-0.002787810517475009, -0.0023808081168681383, 0.006570389028638601]],

                [[-0.01818399503827095, -0.016664784401655197, -0.016933994367718697],
                 [-0.0032500678207725286, -0.002716263523325324, 0.00792204961180687]],

                [[-0.01906922645866871, -0.017558123916387558, -0.017497723922133446],
                 [-0.0034973544534295797, -0.002890110481530428, 0.008606006391346455]],

                [[-0.019496159628033638, -0.017993737012147903, -0.01763434149324894],
                 [-0.0036818813532590866, -0.003022562013939023, 0.009041817858815193]],

                [[-0.01969190314412117, -0.018201317638158798, -0.017547737807035446],

                 [-0.0038449172861874104, -0.003145989030599594, 0.009346261620521545]],

                [[-0.019737228751182556, -0.018264643847942352, -0.0173049159348011],
                 [-0.004004715010523796, -0.003275529947131872, 0.009564205072820187]],

                [[-0.019665192812681198, -0.018219994381070137, -0.01693047396838665],
                 [-0.004172911401838064, -0.0034219594672322273, 0.009713913314044476]],

                [[-0.01949373073875904, -0.01808745414018631, -0.01643970049917698],
                 [-0.004358743317425251, -0.0035946646239608526, 0.009800488129258156]],

                [[-0.019242193549871445, -0.01788627728819847, -0.015856854617595673],
                 [-0.0045697917230427265, -0.0038014191668480635, 0.009822248481214046]],

                [[-0.01894020289182663, -0.017642680555582047, -0.015223790891468525],
                 [-0.004811229649931192, -0.004046828951686621, 0.009775890968739986]],

                [[-0.018637115135788918, -0.017389029264450073, -0.014595868065953255],
                 [-0.005084861535578966, -0.0043313330970704556, 0.00966064352542162]],

                [[-0.018358834087848663, -0.017158253118395805, -0.014026599936187267],
                 [-0.00539231114089489, -0.004652077332139015, 0.009479362517595291]],

                [[-0.018139295279979706, -0.016974788159132004, -0.013552641496062279],
                 [-0.005724799819290638, -0.005007237195968628, 0.009235722944140434]],

                [[-0.01799042522907257, -0.016854379326105118, -0.013189395889639854],
                 [-0.006096957251429558, -0.0053996010683476925, 0.00892884936183691]],

                [[-0.01792767457664013, -0.016808394342660904, -0.01293881144374609],
                 [-0.006511836312711239, -0.005842543672770262, 0.008547094650566578]],

                [[-0.017963677644729614, -0.016854533925652504, -0.012803212739527225],
                 [-0.007028862368315458, -0.0063656410202383995, 0.00805988721549511]],

                [[-0.01813627779483795, -0.017030464485287666, -0.012803859077394009],
                 [-0.007689429447054863, -0.007028832100331783, 0.007404951844364405]],

                [[-0.018535180017352104, -0.01742624118924141, -0.013013389892876148],
                 [-0.008611081168055534, -0.007948571816086769, 0.006469985470175743]],

                [[-0.019416848197579384, -0.01828826777637005, -0.013652382418513298],
                 [-0.010075435042381287, -0.009396139532327652, 0.005024670157581568]],

                [[-0.021592704579234123, -0.02032707817852497, -0.01557872723788023],
                 [-0.012770703993737698, -0.012113306671380997, 0.0024051270447671413]],

                [[-0.015962883830070496, -0.014421091414988041, -0.015121867880225182],
                 [-0.002787810517475009, -0.0023808081168681383, 0.006570389028638601]],

                [[-0.01818399503827095, -0.016664784401655197, -0.016933994367718697],
                 [-0.0032500678207725286, -0.002716263523325324, 0.00792204961180687]],

                [[-0.01906922645866871, -0.017558123916387558, -0.017497723922133446],
                 [-0.0034973544534295797, -0.002890110481530428, 0.008606006391346455]],

                [[-0.019496159628033638, -0.017993737012147903, -0.01763434149324894],
                 [-0.0036818813532590866, -0.003022562013939023, 0.009041817858815193]],

                [[-0.01969190314412117, -0.018201317638158798, -0.017547737807035446],

                 [-0.0038449172861874104, -0.003145989030599594, 0.009346261620521545]],

                [[-0.019737228751182556, -0.018264643847942352, -0.0173049159348011],
                 [-0.004004715010523796, -0.003275529947131872, 0.009564205072820187]],

                [[-0.019665192812681198, -0.018219994381070137, -0.01693047396838665],
                 [-0.004172911401838064, -0.0034219594672322273, 0.009713913314044476]],

                [[-0.01949373073875904, -0.01808745414018631, -0.01643970049917698],
                 [-0.004358743317425251, -0.0035946646239608526, 0.009800488129258156]],

                [[-0.019242193549871445, -0.01788627728819847, -0.015856854617595673],
                 [-0.0045697917230427265, -0.0038014191668480635, 0.009822248481214046]],

                [[-0.01894020289182663, -0.017642680555582047, -0.015223790891468525],
                 [-0.004811229649931192, -0.004046828951686621, 0.009775890968739986]],

                [[-0.018637115135788918, -0.017389029264450073, -0.014595868065953255],
                 [-0.005084861535578966, -0.0043313330970704556, 0.00966064352542162]],

                [[-0.018358834087848663, -0.017158253118395805, -0.014026599936187267],
                 [-0.00539231114089489, -0.004652077332139015, 0.009479362517595291]],

                [[-0.018139295279979706, -0.016974788159132004, -0.013552641496062279],
                 [-0.005724799819290638, -0.005007237195968628, 0.009235722944140434]],

                [[-0.01799042522907257, -0.016854379326105118, -0.013189395889639854],
                 [-0.006096957251429558, -0.0053996010683476925, 0.00892884936183691]],

                [[-0.01792767457664013, -0.016808394342660904, -0.01293881144374609],
                 [-0.006511836312711239, -0.005842543672770262, 0.008547094650566578]],

                [[-0.017963677644729614, -0.016854533925652504, -0.012803212739527225],
                 [-0.007028862368315458, -0.0063656410202383995, 0.00805988721549511]],

                [[-0.01813627779483795, -0.017030464485287666, -0.012803859077394009],
                 [-0.007689429447054863, -0.007028832100331783, 0.007404951844364405]],

                [[-0.018535180017352104, -0.01742624118924141, -0.013013389892876148],
                 [-0.008611081168055534, -0.007948571816086769, 0.006469985470175743]],

                [[-0.019416848197579384, -0.01828826777637005, -0.013652382418513298],
                 [-0.010075435042381287, -0.009396139532327652, 0.005024670157581568]],

                [[-0.021592704579234123, -0.02032707817852497, -0.01557872723788023],
                 [-0.012770703993737698, -0.012113306671380997, 0.0024051270447671413]]]],

        mask=[[[[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]],

               [[False, False, False],
                [False, False, False]]]],
        fill_value=1.2676506e+30,
        dtype='float32'
    )

    depth = numpy.array(

        [
            0, 2, 4, 6, 8, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 125, 150, 200, 250, 300, 350,
            400, 500, 600, 700, 800, 900, 1000, 1250, 1500, 2000, 2500, 3000, 4000, 5000
        ]

    )

    num_x = 3
    num_y = 2

    time_index = 0

    target_depth_surface = 0
    target_depth_default = 4.5
    target_depth_deep = 10

    expected_u_target_depth_default = numpy.ma.array(
        data=[[-0.1885196, -0.20516637, -0.21590865],
              [-0.11407378, -0.12985562, -0.13566523]],
        mask=False,
        fill_value=1e+20)

    expected_v_target_depth_default = numpy.ma.array(
        data=[[-0.01917596, -0.01766703, -0.01753188],
              [-0.00354349, -0.00292322, 0.00871496]],
        mask=False,
        fill_value=1e+20)

    expected_u_target_depth_surface = numpy.ma.array(
        data=[[-0.14429612, -0.15575929, -0.16399005],
              [-0.1333293, -0.13850904, -0.14700627]],
        mask=False,
        fill_value=1e+20)

    expected_v_target_depth_surface = numpy.ma.array(
        data=[[-0.01596288, -0.01442109, -0.01512187],
              [-0.00278781, -0.00238081,  0.00657039]],
        mask=False,
        fill_value=1e+20)

    expected_u_target_depth_deep = numpy.ma.array(
        data=[[-0.21044502, -0.22945917, -0.24108765],
              [-0.12573498, -0.143649, -0.14991251]],
        mask=False,
        fill_value=1e+20)

    expected_v_target_depth_deep = numpy.ma.array(
        data=[[-0.01973723, -0.01826464, -0.01730492],
              [-0.00400472, -0.00327553,  0.00956421]],
        mask=False,
        fill_value=1e+20)

    return VerticalValues(u, v, depth,  num_x, num_y, time_index, target_depth_surface, target_depth_default,
                          target_depth_deep, expected_u_target_depth_default, expected_v_target_depth_default,
                          expected_u_target_depth_surface, expected_v_target_depth_surface,
                          expected_u_target_depth_deep, expected_v_target_depth_deep)


def test_vertical_interpolation_target_depth(vertical_values):
    """Test vertical interpolation of u/v to default target depth."""
    u_target_depth, v_target_depth = vertical_interpolation(vertical_values.u, vertical_values.v, vertical_values.depth,
                                                            vertical_values.num_x, vertical_values.num_y,
                                                            vertical_values.time_index,
                                                            vertical_values.target_depth_default)

    print(f"u_target_depth_default: {u_target_depth}")
    print(f"v_target_depth_default: {v_target_depth}")
    assert numpy.allclose(u_target_depth, vertical_values.expected_u_target_depth_default)
    assert numpy.allclose(v_target_depth, vertical_values.expected_v_target_depth_default)


def test_vertical_interpolation_target_depth_at_surface(vertical_values):
    """Test vertical interpolation of u/v to target depth at surface."""
    u_target_depth, v_target_depth = vertical_interpolation(vertical_values.u, vertical_values.v,
                                                            vertical_values.depth,
                                                            vertical_values.num_x, vertical_values.num_y,
                                                            vertical_values.time_index,
                                                            vertical_values.target_depth_surface)

    print(f"u_target_depth_surface: {u_target_depth}")
    print(f"v_target_depth_surface: {v_target_depth}")
    assert numpy.allclose(u_target_depth, vertical_values.expected_u_target_depth_surface)
    assert numpy.allclose(v_target_depth, vertical_values.expected_v_target_depth_surface)


def test_vertical_interpolation_target_depth_deep(vertical_values):
    """Test vertical interpolation of u/v to deeper target depth."""
    u_target_depth, v_target_depth = vertical_interpolation(vertical_values.u, vertical_values.v, vertical_values.depth,
                                                            vertical_values.num_x, vertical_values.num_y,
                                                            vertical_values.time_index,
                                                            vertical_values.target_depth_deep)

    print(f"u_target_depth_deep: {u_target_depth}")
    print(f"v_target_depth_deep: {v_target_depth}")
    assert numpy.allclose(u_target_depth, vertical_values.expected_u_target_depth_deep)
    assert numpy.allclose(v_target_depth, vertical_values.expected_v_target_depth_deep)
