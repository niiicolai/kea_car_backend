/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
$(document).ready(function() {

    $(".click-title").mouseenter( function(    e){
        e.preventDefault();
        this.style.cursor="pointer";
    });
    $(".click-title").mousedown( function(event){
        event.preventDefault();
    });

    // Ugly code while this script is shared among several pages
    try{
        refreshHitsPerSecond(true);
    } catch(e){}
    try{
        refreshResponseTimeOverTime(true);
    } catch(e){}
    try{
        refreshResponseTimePercentiles();
    } catch(e){}
});


var responseTimePercentilesInfos = {
        data: {"result": {"minY": 896.0, "minX": 0.0, "maxY": 8975.0, "series": [{"data": [[0.0, 896.0], [0.1, 904.0], [0.2, 936.0], [0.3, 950.0], [0.4, 954.0], [0.5, 968.0], [0.6, 977.0], [0.7, 980.0], [0.8, 996.0], [0.9, 1005.0], [1.0, 1006.0], [1.1, 1015.0], [1.2, 1022.0], [1.3, 1025.0], [1.4, 1028.0], [1.5, 1035.0], [1.6, 1036.0], [1.7, 1041.0], [1.8, 1043.0], [1.9, 1045.0], [2.0, 1057.0], [2.1, 1057.0], [2.2, 1059.0], [2.3, 1064.0], [2.4, 1065.0], [2.5, 1065.0], [2.6, 1070.0], [2.7, 1075.0], [2.8, 1081.0], [2.9, 1084.0], [3.0, 1086.0], [3.1, 1087.0], [3.2, 1093.0], [3.3, 1094.0], [3.4, 1098.0], [3.5, 1099.0], [3.6, 1101.0], [3.7, 1102.0], [3.8, 1102.0], [3.9, 1105.0], [4.0, 1107.0], [4.1, 1111.0], [4.2, 1112.0], [4.3, 1113.0], [4.4, 1114.0], [4.5, 1119.0], [4.6, 1121.0], [4.7, 1122.0], [4.8, 1124.0], [4.9, 1126.0], [5.0, 1134.0], [5.1, 1135.0], [5.2, 1136.0], [5.3, 1141.0], [5.4, 1141.0], [5.5, 1144.0], [5.6, 1145.0], [5.7, 1148.0], [5.8, 1148.0], [5.9, 1152.0], [6.0, 1154.0], [6.1, 1157.0], [6.2, 1157.0], [6.3, 1159.0], [6.4, 1162.0], [6.5, 1163.0], [6.6, 1169.0], [6.7, 1173.0], [6.8, 1180.0], [6.9, 1182.0], [7.0, 1183.0], [7.1, 1187.0], [7.2, 1188.0], [7.3, 1191.0], [7.4, 1193.0], [7.5, 1195.0], [7.6, 1196.0], [7.7, 1196.0], [7.8, 1206.0], [7.9, 1207.0], [8.0, 1212.0], [8.1, 1213.0], [8.2, 1214.0], [8.3, 1215.0], [8.4, 1217.0], [8.5, 1219.0], [8.6, 1219.0], [8.7, 1221.0], [8.8, 1223.0], [8.9, 1223.0], [9.0, 1225.0], [9.1, 1225.0], [9.2, 1226.0], [9.3, 1227.0], [9.4, 1230.0], [9.5, 1232.0], [9.6, 1235.0], [9.7, 1235.0], [9.8, 1237.0], [9.9, 1244.0], [10.0, 1245.0], [10.1, 1248.0], [10.2, 1250.0], [10.3, 1251.0], [10.4, 1252.0], [10.5, 1252.0], [10.6, 1254.0], [10.7, 1255.0], [10.8, 1260.0], [10.9, 1263.0], [11.0, 1268.0], [11.1, 1270.0], [11.2, 1273.0], [11.3, 1278.0], [11.4, 1279.0], [11.5, 1281.0], [11.6, 1282.0], [11.7, 1286.0], [11.8, 1287.0], [11.9, 1290.0], [12.0, 1295.0], [12.1, 1303.0], [12.2, 1306.0], [12.3, 1308.0], [12.4, 1312.0], [12.5, 1316.0], [12.6, 1317.0], [12.7, 1320.0], [12.8, 1323.0], [12.9, 1336.0], [13.0, 1337.0], [13.1, 1341.0], [13.2, 1346.0], [13.3, 1347.0], [13.4, 1349.0], [13.5, 1357.0], [13.6, 1363.0], [13.7, 1366.0], [13.8, 1404.0], [13.9, 1412.0], [14.0, 1426.0], [14.1, 1430.0], [14.2, 1433.0], [14.3, 1447.0], [14.4, 1454.0], [14.5, 1460.0], [14.6, 1460.0], [14.7, 1462.0], [14.8, 1463.0], [14.9, 1469.0], [15.0, 1470.0], [15.1, 1474.0], [15.2, 1478.0], [15.3, 1481.0], [15.4, 1486.0], [15.5, 1488.0], [15.6, 1495.0], [15.7, 1497.0], [15.8, 1498.0], [15.9, 1502.0], [16.0, 1505.0], [16.1, 1508.0], [16.2, 1514.0], [16.3, 1515.0], [16.4, 1515.0], [16.5, 1520.0], [16.6, 1528.0], [16.7, 1530.0], [16.8, 1534.0], [16.9, 1536.0], [17.0, 1539.0], [17.1, 1541.0], [17.2, 1543.0], [17.3, 1547.0], [17.4, 1548.0], [17.5, 1551.0], [17.6, 1552.0], [17.7, 1557.0], [17.8, 1557.0], [17.9, 1559.0], [18.0, 1560.0], [18.1, 1562.0], [18.2, 1566.0], [18.3, 1566.0], [18.4, 1567.0], [18.5, 1568.0], [18.6, 1573.0], [18.7, 1574.0], [18.8, 1574.0], [18.9, 1576.0], [19.0, 1576.0], [19.1, 1579.0], [19.2, 1581.0], [19.3, 1584.0], [19.4, 1584.0], [19.5, 1585.0], [19.6, 1586.0], [19.7, 1587.0], [19.8, 1588.0], [19.9, 1588.0], [20.0, 1588.0], [20.1, 1590.0], [20.2, 1591.0], [20.3, 1592.0], [20.4, 1593.0], [20.5, 1594.0], [20.6, 1595.0], [20.7, 1596.0], [20.8, 1597.0], [20.9, 1598.0], [21.0, 1600.0], [21.1, 1601.0], [21.2, 1602.0], [21.3, 1602.0], [21.4, 1605.0], [21.5, 1606.0], [21.6, 1606.0], [21.7, 1608.0], [21.8, 1608.0], [21.9, 1611.0], [22.0, 1611.0], [22.1, 1612.0], [22.2, 1615.0], [22.3, 1615.0], [22.4, 1617.0], [22.5, 1617.0], [22.6, 1620.0], [22.7, 1620.0], [22.8, 1622.0], [22.9, 1622.0], [23.0, 1623.0], [23.1, 1624.0], [23.2, 1627.0], [23.3, 1631.0], [23.4, 1631.0], [23.5, 1632.0], [23.6, 1632.0], [23.7, 1632.0], [23.8, 1633.0], [23.9, 1634.0], [24.0, 1635.0], [24.1, 1636.0], [24.2, 1637.0], [24.3, 1639.0], [24.4, 1640.0], [24.5, 1640.0], [24.6, 1641.0], [24.7, 1641.0], [24.8, 1643.0], [24.9, 1644.0], [25.0, 1644.0], [25.1, 1645.0], [25.2, 1646.0], [25.3, 1648.0], [25.4, 1648.0], [25.5, 1648.0], [25.6, 1649.0], [25.7, 1649.0], [25.8, 1650.0], [25.9, 1650.0], [26.0, 1650.0], [26.1, 1651.0], [26.2, 1655.0], [26.3, 1656.0], [26.4, 1659.0], [26.5, 1660.0], [26.6, 1660.0], [26.7, 1663.0], [26.8, 1663.0], [26.9, 1665.0], [27.0, 1668.0], [27.1, 1668.0], [27.2, 1669.0], [27.3, 1670.0], [27.4, 1670.0], [27.5, 1671.0], [27.6, 1673.0], [27.7, 1674.0], [27.8, 1675.0], [27.9, 1676.0], [28.0, 1677.0], [28.1, 1678.0], [28.2, 1679.0], [28.3, 1680.0], [28.4, 1680.0], [28.5, 1681.0], [28.6, 1682.0], [28.7, 1683.0], [28.8, 1684.0], [28.9, 1684.0], [29.0, 1687.0], [29.1, 1687.0], [29.2, 1688.0], [29.3, 1688.0], [29.4, 1689.0], [29.5, 1689.0], [29.6, 1689.0], [29.7, 1689.0], [29.8, 1691.0], [29.9, 1692.0], [30.0, 1693.0], [30.1, 1695.0], [30.2, 1695.0], [30.3, 1696.0], [30.4, 1698.0], [30.5, 1698.0], [30.6, 1699.0], [30.7, 1699.0], [30.8, 1700.0], [30.9, 1701.0], [31.0, 1701.0], [31.1, 1702.0], [31.2, 1702.0], [31.3, 1704.0], [31.4, 1705.0], [31.5, 1706.0], [31.6, 1707.0], [31.7, 1708.0], [31.8, 1711.0], [31.9, 1711.0], [32.0, 1712.0], [32.1, 1712.0], [32.2, 1713.0], [32.3, 1714.0], [32.4, 1715.0], [32.5, 1716.0], [32.6, 1717.0], [32.7, 1719.0], [32.8, 1720.0], [32.9, 1721.0], [33.0, 1723.0], [33.1, 1724.0], [33.2, 1724.0], [33.3, 1725.0], [33.4, 1726.0], [33.5, 1726.0], [33.6, 1727.0], [33.7, 1730.0], [33.8, 1730.0], [33.9, 1730.0], [34.0, 1730.0], [34.1, 1732.0], [34.2, 1733.0], [34.3, 1734.0], [34.4, 1736.0], [34.5, 1737.0], [34.6, 1738.0], [34.7, 1739.0], [34.8, 1739.0], [34.9, 1740.0], [35.0, 1740.0], [35.1, 1741.0], [35.2, 1742.0], [35.3, 1743.0], [35.4, 1743.0], [35.5, 1744.0], [35.6, 1744.0], [35.7, 1744.0], [35.8, 1744.0], [35.9, 1751.0], [36.0, 1751.0], [36.1, 1753.0], [36.2, 1754.0], [36.3, 1755.0], [36.4, 1760.0], [36.5, 1760.0], [36.6, 1761.0], [36.7, 1763.0], [36.8, 1763.0], [36.9, 1764.0], [37.0, 1764.0], [37.1, 1764.0], [37.2, 1764.0], [37.3, 1765.0], [37.4, 1765.0], [37.5, 1765.0], [37.6, 1766.0], [37.7, 1767.0], [37.8, 1768.0], [37.9, 1769.0], [38.0, 1770.0], [38.1, 1772.0], [38.2, 1772.0], [38.3, 1773.0], [38.4, 1773.0], [38.5, 1774.0], [38.6, 1775.0], [38.7, 1776.0], [38.8, 1776.0], [38.9, 1777.0], [39.0, 1778.0], [39.1, 1778.0], [39.2, 1779.0], [39.3, 1779.0], [39.4, 1780.0], [39.5, 1780.0], [39.6, 1781.0], [39.7, 1782.0], [39.8, 1782.0], [39.9, 1783.0], [40.0, 1783.0], [40.1, 1786.0], [40.2, 1786.0], [40.3, 1787.0], [40.4, 1787.0], [40.5, 1788.0], [40.6, 1792.0], [40.7, 1793.0], [40.8, 1793.0], [40.9, 1793.0], [41.0, 1794.0], [41.1, 1797.0], [41.2, 1797.0], [41.3, 1798.0], [41.4, 1798.0], [41.5, 1800.0], [41.6, 1800.0], [41.7, 1801.0], [41.8, 1801.0], [41.9, 1802.0], [42.0, 1802.0], [42.1, 1803.0], [42.2, 1804.0], [42.3, 1805.0], [42.4, 1807.0], [42.5, 1807.0], [42.6, 1808.0], [42.7, 1809.0], [42.8, 1811.0], [42.9, 1812.0], [43.0, 1812.0], [43.1, 1813.0], [43.2, 1814.0], [43.3, 1815.0], [43.4, 1818.0], [43.5, 1820.0], [43.6, 1823.0], [43.7, 1824.0], [43.8, 1827.0], [43.9, 1828.0], [44.0, 1828.0], [44.1, 1834.0], [44.2, 1838.0], [44.3, 1842.0], [44.4, 1843.0], [44.5, 1844.0], [44.6, 1852.0], [44.7, 1855.0], [44.8, 1855.0], [44.9, 1856.0], [45.0, 1861.0], [45.1, 1862.0], [45.2, 1862.0], [45.3, 1863.0], [45.4, 1867.0], [45.5, 1868.0], [45.6, 1868.0], [45.7, 1872.0], [45.8, 1874.0], [45.9, 1877.0], [46.0, 1877.0], [46.1, 1880.0], [46.2, 1883.0], [46.3, 1884.0], [46.4, 1887.0], [46.5, 1890.0], [46.6, 1894.0], [46.7, 1894.0], [46.8, 1900.0], [46.9, 1900.0], [47.0, 1903.0], [47.1, 1908.0], [47.2, 1911.0], [47.3, 1913.0], [47.4, 1913.0], [47.5, 1914.0], [47.6, 1916.0], [47.7, 1928.0], [47.8, 1932.0], [47.9, 1935.0], [48.0, 1939.0], [48.1, 1941.0], [48.2, 1944.0], [48.3, 1946.0], [48.4, 1951.0], [48.5, 1952.0], [48.6, 1963.0], [48.7, 1965.0], [48.8, 1965.0], [48.9, 1973.0], [49.0, 1975.0], [49.1, 1983.0], [49.2, 1984.0], [49.3, 1990.0], [49.4, 1997.0], [49.5, 1997.0], [49.6, 2001.0], [49.7, 2005.0], [49.8, 2010.0], [49.9, 2013.0], [50.0, 2016.0], [50.1, 2021.0], [50.2, 2034.0], [50.3, 2036.0], [50.4, 2048.0], [50.5, 2055.0], [50.6, 2056.0], [50.7, 2066.0], [50.8, 2075.0], [50.9, 2077.0], [51.0, 2077.0], [51.1, 2081.0], [51.2, 2084.0], [51.3, 2088.0], [51.4, 2096.0], [51.5, 2109.0], [51.6, 2119.0], [51.7, 2126.0], [51.8, 2127.0], [51.9, 2135.0], [52.0, 2136.0], [52.1, 2141.0], [52.2, 2151.0], [52.3, 2153.0], [52.4, 2156.0], [52.5, 2156.0], [52.6, 2163.0], [52.7, 2165.0], [52.8, 2170.0], [52.9, 2171.0], [53.0, 2174.0], [53.1, 2176.0], [53.2, 2178.0], [53.3, 2181.0], [53.4, 2184.0], [53.5, 2188.0], [53.6, 2192.0], [53.7, 2196.0], [53.8, 2198.0], [53.9, 2204.0], [54.0, 2205.0], [54.1, 2208.0], [54.2, 2210.0], [54.3, 2210.0], [54.4, 2213.0], [54.5, 2216.0], [54.6, 2216.0], [54.7, 2217.0], [54.8, 2218.0], [54.9, 2221.0], [55.0, 2222.0], [55.1, 2222.0], [55.2, 2225.0], [55.3, 2229.0], [55.4, 2230.0], [55.5, 2233.0], [55.6, 2237.0], [55.7, 2238.0], [55.8, 2240.0], [55.9, 2240.0], [56.0, 2246.0], [56.1, 2251.0], [56.2, 2253.0], [56.3, 2254.0], [56.4, 2254.0], [56.5, 2258.0], [56.6, 2259.0], [56.7, 2264.0], [56.8, 2268.0], [56.9, 2270.0], [57.0, 2272.0], [57.1, 2273.0], [57.2, 2277.0], [57.3, 2278.0], [57.4, 2279.0], [57.5, 2284.0], [57.6, 2285.0], [57.7, 2287.0], [57.8, 2289.0], [57.9, 2290.0], [58.0, 2291.0], [58.1, 2292.0], [58.2, 2292.0], [58.3, 2293.0], [58.4, 2296.0], [58.5, 2298.0], [58.6, 2304.0], [58.7, 2305.0], [58.8, 2305.0], [58.9, 2306.0], [59.0, 2309.0], [59.1, 2310.0], [59.2, 2311.0], [59.3, 2315.0], [59.4, 2318.0], [59.5, 2319.0], [59.6, 2320.0], [59.7, 2324.0], [59.8, 2327.0], [59.9, 2328.0], [60.0, 2329.0], [60.1, 2331.0], [60.2, 2337.0], [60.3, 2339.0], [60.4, 2344.0], [60.5, 2345.0], [60.6, 2346.0], [60.7, 2347.0], [60.8, 2349.0], [60.9, 2351.0], [61.0, 2353.0], [61.1, 2357.0], [61.2, 2360.0], [61.3, 2360.0], [61.4, 2362.0], [61.5, 2364.0], [61.6, 2367.0], [61.7, 2367.0], [61.8, 2368.0], [61.9, 2368.0], [62.0, 2375.0], [62.1, 2376.0], [62.2, 2377.0], [62.3, 2380.0], [62.4, 2380.0], [62.5, 2381.0], [62.6, 2382.0], [62.7, 2385.0], [62.8, 2385.0], [62.9, 2386.0], [63.0, 2387.0], [63.1, 2388.0], [63.2, 2392.0], [63.3, 2392.0], [63.4, 2394.0], [63.5, 2397.0], [63.6, 2401.0], [63.7, 2405.0], [63.8, 2408.0], [63.9, 2411.0], [64.0, 2413.0], [64.1, 2415.0], [64.2, 2417.0], [64.3, 2418.0], [64.4, 2424.0], [64.5, 2424.0], [64.6, 2428.0], [64.7, 2429.0], [64.8, 2436.0], [64.9, 2441.0], [65.0, 2445.0], [65.1, 2446.0], [65.2, 2449.0], [65.3, 2451.0], [65.4, 2454.0], [65.5, 2456.0], [65.6, 2457.0], [65.7, 2464.0], [65.8, 2465.0], [65.9, 2467.0], [66.0, 2469.0], [66.1, 2469.0], [66.2, 2470.0], [66.3, 2470.0], [66.4, 2472.0], [66.5, 2474.0], [66.6, 2474.0], [66.7, 2478.0], [66.8, 2480.0], [66.9, 2483.0], [67.0, 2487.0], [67.1, 2493.0], [67.2, 2494.0], [67.3, 2495.0], [67.4, 2499.0], [67.5, 2512.0], [67.6, 2517.0], [67.7, 2518.0], [67.8, 2521.0], [67.9, 2526.0], [68.0, 2530.0], [68.1, 2534.0], [68.2, 2534.0], [68.3, 2541.0], [68.4, 2544.0], [68.5, 2548.0], [68.6, 2548.0], [68.7, 2551.0], [68.8, 2561.0], [68.9, 2563.0], [69.0, 2574.0], [69.1, 2577.0], [69.2, 2591.0], [69.3, 2593.0], [69.4, 2602.0], [69.5, 2604.0], [69.6, 2604.0], [69.7, 2614.0], [69.8, 2632.0], [69.9, 2647.0], [70.0, 2654.0], [70.1, 2658.0], [70.2, 2666.0], [70.3, 2669.0], [70.4, 2681.0], [70.5, 2688.0], [70.6, 2692.0], [70.7, 2696.0], [70.8, 2699.0], [70.9, 2702.0], [71.0, 2703.0], [71.1, 2715.0], [71.2, 2718.0], [71.3, 2726.0], [71.4, 2729.0], [71.5, 2739.0], [71.6, 2741.0], [71.7, 2748.0], [71.8, 2755.0], [71.9, 2758.0], [72.0, 2758.0], [72.1, 2759.0], [72.2, 2760.0], [72.3, 2761.0], [72.4, 2769.0], [72.5, 2781.0], [72.6, 2782.0], [72.7, 2789.0], [72.8, 2794.0], [72.9, 2799.0], [73.0, 2804.0], [73.1, 2808.0], [73.2, 2817.0], [73.3, 2819.0], [73.4, 2826.0], [73.5, 2831.0], [73.6, 2833.0], [73.7, 2834.0], [73.8, 2837.0], [73.9, 2843.0], [74.0, 2846.0], [74.1, 2852.0], [74.2, 2856.0], [74.3, 2862.0], [74.4, 2863.0], [74.5, 2868.0], [74.6, 2871.0], [74.7, 2878.0], [74.8, 2878.0], [74.9, 2879.0], [75.0, 2884.0], [75.1, 2889.0], [75.2, 2892.0], [75.3, 2894.0], [75.4, 2900.0], [75.5, 2908.0], [75.6, 2914.0], [75.7, 2924.0], [75.8, 2924.0], [75.9, 2928.0], [76.0, 2931.0], [76.1, 2934.0], [76.2, 2943.0], [76.3, 2950.0], [76.4, 2959.0], [76.5, 2961.0], [76.6, 2966.0], [76.7, 2968.0], [76.8, 2971.0], [76.9, 2973.0], [77.0, 2974.0], [77.1, 2986.0], [77.2, 2987.0], [77.3, 2991.0], [77.4, 2997.0], [77.5, 3003.0], [77.6, 3012.0], [77.7, 3016.0], [77.8, 3020.0], [77.9, 3020.0], [78.0, 3025.0], [78.1, 3028.0], [78.2, 3035.0], [78.3, 3037.0], [78.4, 3044.0], [78.5, 3047.0], [78.6, 3051.0], [78.7, 3065.0], [78.8, 3070.0], [78.9, 3084.0], [79.0, 3088.0], [79.1, 3097.0], [79.2, 3109.0], [79.3, 3111.0], [79.4, 3112.0], [79.5, 3116.0], [79.6, 3120.0], [79.7, 3129.0], [79.8, 3143.0], [79.9, 3145.0], [80.0, 3149.0], [80.1, 3151.0], [80.2, 3154.0], [80.3, 3165.0], [80.4, 3166.0], [80.5, 3168.0], [80.6, 3185.0], [80.7, 3188.0], [80.8, 3191.0], [80.9, 3197.0], [81.0, 3202.0], [81.1, 3203.0], [81.2, 3205.0], [81.3, 3206.0], [81.4, 3221.0], [81.5, 3234.0], [81.6, 3243.0], [81.7, 3252.0], [81.8, 3253.0], [81.9, 3256.0], [82.0, 3271.0], [82.1, 3286.0], [82.2, 3294.0], [82.3, 3296.0], [82.4, 3297.0], [82.5, 3297.0], [82.6, 3310.0], [82.7, 3326.0], [82.8, 3338.0], [82.9, 3348.0], [83.0, 3350.0], [83.1, 3352.0], [83.2, 3355.0], [83.3, 3369.0], [83.4, 3372.0], [83.5, 3390.0], [83.6, 3400.0], [83.7, 3403.0], [83.8, 3419.0], [83.9, 3430.0], [84.0, 3448.0], [84.1, 3451.0], [84.2, 3468.0], [84.3, 3469.0], [84.4, 3474.0], [84.5, 3484.0], [84.6, 3486.0], [84.7, 3489.0], [84.8, 3495.0], [84.9, 3506.0], [85.0, 3515.0], [85.1, 3518.0], [85.2, 3532.0], [85.3, 3548.0], [85.4, 3549.0], [85.5, 3550.0], [85.6, 3558.0], [85.7, 3561.0], [85.8, 3561.0], [85.9, 3563.0], [86.0, 3565.0], [86.1, 3571.0], [86.2, 3571.0], [86.3, 3582.0], [86.4, 3586.0], [86.5, 3590.0], [86.6, 3595.0], [86.7, 3602.0], [86.8, 3605.0], [86.9, 3609.0], [87.0, 3626.0], [87.1, 3627.0], [87.2, 3634.0], [87.3, 3637.0], [87.4, 3642.0], [87.5, 3647.0], [87.6, 3648.0], [87.7, 3650.0], [87.8, 3653.0], [87.9, 3655.0], [88.0, 3657.0], [88.1, 3667.0], [88.2, 3675.0], [88.3, 3677.0], [88.4, 3681.0], [88.5, 3681.0], [88.6, 3686.0], [88.7, 3701.0], [88.8, 3705.0], [88.9, 3706.0], [89.0, 3709.0], [89.1, 3711.0], [89.2, 3713.0], [89.3, 3722.0], [89.4, 3727.0], [89.5, 3735.0], [89.6, 3738.0], [89.7, 3744.0], [89.8, 3749.0], [89.9, 3751.0], [90.0, 3757.0], [90.1, 3758.0], [90.2, 3760.0], [90.3, 3763.0], [90.4, 3764.0], [90.5, 3766.0], [90.6, 3766.0], [90.7, 3769.0], [90.8, 3776.0], [90.9, 3778.0], [91.0, 3786.0], [91.1, 3794.0], [91.2, 3797.0], [91.3, 3802.0], [91.4, 3806.0], [91.5, 3814.0], [91.6, 3820.0], [91.7, 3821.0], [91.8, 3827.0], [91.9, 3838.0], [92.0, 3839.0], [92.1, 3843.0], [92.2, 3847.0], [92.3, 3851.0], [92.4, 3852.0], [92.5, 3858.0], [92.6, 3873.0], [92.7, 3888.0], [92.8, 3896.0], [92.9, 3900.0], [93.0, 3904.0], [93.1, 3905.0], [93.2, 3907.0], [93.3, 3916.0], [93.4, 3921.0], [93.5, 3929.0], [93.6, 3939.0], [93.7, 3948.0], [93.8, 3950.0], [93.9, 3957.0], [94.0, 3967.0], [94.1, 3982.0], [94.2, 4014.0], [94.3, 4015.0], [94.4, 4016.0], [94.5, 4022.0], [94.6, 4042.0], [94.7, 4045.0], [94.8, 4049.0], [94.9, 4056.0], [95.0, 4057.0], [95.1, 4080.0], [95.2, 4085.0], [95.3, 4091.0], [95.4, 4095.0], [95.5, 4102.0], [95.6, 4113.0], [95.7, 4116.0], [95.8, 4125.0], [95.9, 4126.0], [96.0, 4132.0], [96.1, 4133.0], [96.2, 4142.0], [96.3, 4147.0], [96.4, 4149.0], [96.5, 4159.0], [96.6, 4159.0], [96.7, 4178.0], [96.8, 4179.0], [96.9, 4204.0], [97.0, 4217.0], [97.1, 4257.0], [97.2, 4270.0], [97.3, 4285.0], [97.4, 4298.0], [97.5, 4299.0], [97.6, 4328.0], [97.7, 4343.0], [97.8, 4353.0], [97.9, 4375.0], [98.0, 4382.0], [98.1, 4395.0], [98.2, 4408.0], [98.3, 4511.0], [98.4, 4519.0], [98.5, 4558.0], [98.6, 4566.0], [98.7, 4578.0], [98.8, 4583.0], [98.9, 4586.0], [99.0, 4621.0], [99.1, 4622.0], [99.2, 4637.0], [99.3, 4784.0], [99.4, 5197.0], [99.5, 5867.0], [99.6, 5910.0], [99.7, 7677.0], [99.8, 7742.0], [99.9, 8441.0], [100.0, 8975.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "maxX": 100.0, "title": "Response Time Percentiles"}},
        getOptions: function() {
            return {
                series: {
                    points: { show: false }
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimePercentiles'
                },
                xaxis: {
                    tickDecimals: 1,
                    axisLabel: "Percentiles",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Percentile value in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : %x.2 percentile was %y ms"
                },
                selection: { mode: "xy" },
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesResponseTimePercentiles"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimesPercentiles"), dataset, options);
            // setup overview
            $.plot($("#overviewResponseTimesPercentiles"), dataset, prepareOverviewOptions(options));
        }
};

/**
 * @param elementId Id of element where we display message
 */
function setEmptyGraph(elementId) {
    $(function() {
        $(elementId).text("No graph series with filter="+seriesFilter);
    });
}

// Response times percentiles
function refreshResponseTimePercentiles() {
    var infos = responseTimePercentilesInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyResponseTimePercentiles");
        return;
    }
    if (isGraph($("#flotResponseTimesPercentiles"))){
        infos.createGraph();
    } else {
        var choiceContainer = $("#choicesResponseTimePercentiles");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimesPercentiles", "#overviewResponseTimesPercentiles");
        $('#bodyResponseTimePercentiles .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
}

var responseTimeDistributionInfos = {
        data: {"result": {"minY": 1.0, "minX": 800.0, "maxY": 168.0, "series": [{"data": [[800.0, 1.0], [900.0, 12.0], [1000.0, 42.0], [1100.0, 66.0], [1200.0, 68.0], [1300.0, 26.0], [1400.0, 33.0], [1500.0, 81.0], [1600.0, 153.0], [1700.0, 168.0], [1800.0, 83.0], [1900.0, 44.0], [2000.0, 29.0], [2100.0, 38.0], [2200.0, 74.0], [2300.0, 78.0], [2400.0, 61.0], [2500.0, 30.0], [2600.0, 23.0], [2700.0, 33.0], [2800.0, 38.0], [2900.0, 33.0], [3000.0, 27.0], [3100.0, 28.0], [3300.0, 17.0], [3200.0, 24.0], [3400.0, 19.0], [3500.0, 29.0], [3700.0, 41.0], [3600.0, 31.0], [3800.0, 25.0], [3900.0, 20.0], [4000.0, 21.0], [4300.0, 10.0], [4100.0, 22.0], [4200.0, 10.0], [4500.0, 10.0], [4600.0, 6.0], [4400.0, 2.0], [4700.0, 1.0], [5100.0, 1.0], [5600.0, 1.0], [5800.0, 1.0], [5900.0, 1.0], [7500.0, 1.0], [7600.0, 1.0], [7700.0, 1.0], [7800.0, 1.0], [8400.0, 1.0], [8900.0, 1.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 100, "maxX": 8900.0, "title": "Response Time Distribution"}},
        getOptions: function() {
            var granularity = this.data.result.granularity;
            return {
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimeDistribution'
                },
                xaxis:{
                    axisLabel: "Response times in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of responses",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                bars : {
                    show: true,
                    barWidth: this.data.result.granularity
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: function(label, xval, yval, flotItem){
                        return yval + " responses for " + label + " were between " + xval + " and " + (xval + granularity) + " ms";
                    }
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimeDistribution"), prepareData(data.result.series, $("#choicesResponseTimeDistribution")), options);
        }

};

// Response time distribution
function refreshResponseTimeDistribution() {
    var infos = responseTimeDistributionInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyResponseTimeDistribution");
        return;
    }
    if (isGraph($("#flotResponseTimeDistribution"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesResponseTimeDistribution");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        $('#footerResponseTimeDistribution .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};


var syntheticResponseTimeDistributionInfos = {
        data: {"result": {"minY": 248.0, "minX": 1.0, "ticks": [[0, "Requests having \nresponse time <= 500ms"], [1, "Requests having \nresponse time > 500ms and <= 1,500ms"], [2, "Requests having \nresponse time > 1,500ms"], [3, "Requests in error"]], "maxY": 1319.0, "series": [{"data": [], "color": "#9ACD32", "isOverall": false, "label": "Requests having \nresponse time <= 500ms", "isController": false}, {"data": [[1.0, 248.0]], "color": "yellow", "isOverall": false, "label": "Requests having \nresponse time > 500ms and <= 1,500ms", "isController": false}, {"data": [[2.0, 1319.0]], "color": "orange", "isOverall": false, "label": "Requests having \nresponse time > 1,500ms", "isController": false}, {"data": [], "color": "#FF6347", "isOverall": false, "label": "Requests in error", "isController": false}], "supportsControllersDiscrimination": false, "maxX": 2.0, "title": "Synthetic Response Times Distribution"}},
        getOptions: function() {
            return {
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendSyntheticResponseTimeDistribution'
                },
                xaxis:{
                    axisLabel: "Response times ranges",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                    tickLength:0,
                    min:-0.5,
                    max:3.5
                },
                yaxis: {
                    axisLabel: "Number of responses",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                bars : {
                    show: true,
                    align: "center",
                    barWidth: 0.25,
                    fill:.75
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: function(label, xval, yval, flotItem){
                        return yval + " " + label;
                    }
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var options = this.getOptions();
            prepareOptions(options, data);
            options.xaxis.ticks = data.result.ticks;
            $.plot($("#flotSyntheticResponseTimeDistribution"), prepareData(data.result.series, $("#choicesSyntheticResponseTimeDistribution")), options);
        }

};

// Response time distribution
function refreshSyntheticResponseTimeDistribution() {
    var infos = syntheticResponseTimeDistributionInfos;
    prepareSeries(infos.data, true);
    if (isGraph($("#flotSyntheticResponseTimeDistribution"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesSyntheticResponseTimeDistribution");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        $('#footerSyntheticResponseTimeDistribution .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var activeThreadsOverTimeInfos = {
        data: {"result": {"minY": 1.5, "minX": 1.73551752E12, "maxY": 2.0, "series": [{"data": [[1.73551782E12, 2.0], [1.73551812E12, 2.0], [1.73551764E12, 2.0], [1.73551794E12, 2.0], [1.73551776E12, 2.0], [1.73551758E12, 2.0], [1.73551806E12, 2.0], [1.73551788E12, 2.0], [1.7355177E12, 2.0], [1.73551752E12, 2.0], [1.735518E12, 2.0]], "isOverall": false, "label": "bzm - Concurrency Thread Group (Login Test)-ThreadStarter", "isController": false}, {"data": [[1.73551782E12, 2.0], [1.73551812E12, 1.5], [1.73551764E12, 2.0], [1.73551794E12, 2.0], [1.73551776E12, 2.0], [1.73551758E12, 2.0], [1.73551806E12, 2.0], [1.73551788E12, 2.0], [1.7355177E12, 2.0], [1.73551752E12, 2.0], [1.735518E12, 2.0]], "isOverall": false, "label": "bzm - Concurrency Thread Group (Create Customer Test)-ThreadStarter", "isController": false}, {"data": [[1.73551782E12, 2.0], [1.73551812E12, 2.0], [1.73551764E12, 2.0], [1.73551794E12, 2.0], [1.73551776E12, 2.0], [1.73551758E12, 2.0], [1.73551806E12, 2.0], [1.73551788E12, 2.0], [1.7355177E12, 2.0], [1.73551752E12, 2.0], [1.735518E12, 2.0]], "isOverall": false, "label": "bzm - Concurrency Thread Group (View Cars Test)-ThreadStarter", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551812E12, "title": "Active Threads Over Time"}},
        getOptions: function() {
            return {
                series: {
                    stack: true,
                    lines: {
                        show: true,
                        fill: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of active threads",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 6,
                    show: true,
                    container: '#legendActiveThreadsOverTime'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                selection: {
                    mode: 'xy'
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : At %x there were %y active threads"
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesActiveThreadsOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotActiveThreadsOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewActiveThreadsOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Active Threads Over Time
function refreshActiveThreadsOverTime(fixTimestamps) {
    var infos = activeThreadsOverTimeInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 3600000);
    }
    if(isGraph($("#flotActiveThreadsOverTime"))) {
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesActiveThreadsOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotActiveThreadsOverTime", "#overviewActiveThreadsOverTime");
        $('#footerActiveThreadsOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var timeVsThreadsInfos = {
        data: {"result": {"minY": 1695.5, "minX": 2.0, "maxY": 3802.0, "series": [{"data": [[4.0, 3802.0], [2.0, 2124.0], [5.0, 1695.5], [6.0, 2312.1600512163877]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}, {"data": [[5.992342054881941, 2312.0835992342036]], "isOverall": false, "label": "jp@gc - WebDriver Sampler-Aggregated", "isController": false}], "supportsControllersDiscrimination": true, "maxX": 6.0, "title": "Time VS Threads"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    axisLabel: "Number of active threads",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average response times in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: { noColumns: 2,show: true, container: '#legendTimeVsThreads' },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s: At %x.2 active threads, Average response time was %y.2 ms"
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesTimeVsThreads"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotTimesVsThreads"), dataset, options);
            // setup overview
            $.plot($("#overviewTimesVsThreads"), dataset, prepareOverviewOptions(options));
        }
};

// Time vs threads
function refreshTimeVsThreads(){
    var infos = timeVsThreadsInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyTimeVsThreads");
        return;
    }
    if(isGraph($("#flotTimesVsThreads"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesTimeVsThreads");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotTimesVsThreads", "#overviewTimesVsThreads");
        $('#footerTimeVsThreads .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var bytesThroughputOverTimeInfos = {
        data : {"result": {"minY": 0.0, "minX": 1.73551752E12, "maxY": 222441.5, "series": [{"data": [[1.73551782E12, 186112.91666666666], [1.73551812E12, 12696.983333333334], [1.73551764E12, 187604.41666666666], [1.73551794E12, 180293.86666666667], [1.73551776E12, 189905.16666666666], [1.73551758E12, 183167.46666666667], [1.73551806E12, 222441.5], [1.73551788E12, 187698.65], [1.7355177E12, 183571.15], [1.73551752E12, 209898.0], [1.735518E12, 186571.21666666667]], "isOverall": false, "label": "Bytes received per second", "isController": false}, {"data": [[1.73551782E12, 0.0], [1.73551812E12, 0.0], [1.73551764E12, 0.0], [1.73551794E12, 0.0], [1.73551776E12, 0.0], [1.73551758E12, 0.0], [1.73551806E12, 0.0], [1.73551788E12, 0.0], [1.7355177E12, 0.0], [1.73551752E12, 0.0], [1.735518E12, 0.0]], "isOverall": false, "label": "Bytes sent per second", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551812E12, "title": "Bytes Throughput Over Time"}},
        getOptions : function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity) ,
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Bytes / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendBytesThroughputOverTime'
                },
                selection: {
                    mode: "xy"
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y"
                }
            };
        },
        createGraph : function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesBytesThroughputOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotBytesThroughputOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewBytesThroughputOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Bytes throughput Over Time
function refreshBytesThroughputOverTime(fixTimestamps) {
    var infos = bytesThroughputOverTimeInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 3600000);
    }
    if(isGraph($("#flotBytesThroughputOverTime"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesBytesThroughputOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotBytesThroughputOverTime", "#overviewBytesThroughputOverTime");
        $('#footerBytesThroughputOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
}

var responseTimesOverTimeInfos = {
        data: {"result": {"minY": 2218.3999999999996, "minX": 1.73551752E12, "maxY": 2373.9144736842095, "series": [{"data": [[1.73551782E12, 2306.0886075949365], [1.73551812E12, 2218.3999999999996], [1.73551764E12, 2282.2151898734187], [1.73551794E12, 2302.3486842105262], [1.73551776E12, 2237.289308176101], [1.73551758E12, 2339.118421052632], [1.73551806E12, 2286.6772151898736], [1.73551788E12, 2313.9999999999995], [1.7355177E12, 2359.142857142858], [1.73551752E12, 2373.9144736842095], [1.735518E12, 2330.664556962025]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551812E12, "title": "Response Time Over Time"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average response time in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimesOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Average response time was %y ms"
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesResponseTimesOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimesOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewResponseTimesOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Response Times Over Time
function refreshResponseTimeOverTime(fixTimestamps) {
    var infos = responseTimesOverTimeInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyResponseTimeOverTime");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 3600000);
    }
    if(isGraph($("#flotResponseTimesOverTime"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesResponseTimesOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimesOverTime", "#overviewResponseTimesOverTime");
        $('#footerResponseTimesOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var latenciesOverTimeInfos = {
        data: {"result": {"minY": 0.0, "minX": 1.73551752E12, "maxY": 4.9E-324, "series": [{"data": [[1.73551782E12, 0.0], [1.73551812E12, 0.0], [1.73551764E12, 0.0], [1.73551794E12, 0.0], [1.73551776E12, 0.0], [1.73551758E12, 0.0], [1.73551806E12, 0.0], [1.73551788E12, 0.0], [1.7355177E12, 0.0], [1.73551752E12, 0.0], [1.735518E12, 0.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551812E12, "title": "Latencies Over Time"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average response latencies in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendLatenciesOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Average latency was %y ms"
                }
            };
        },
        createGraph: function () {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesLatenciesOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotLatenciesOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewLatenciesOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Latencies Over Time
function refreshLatenciesOverTime(fixTimestamps) {
    var infos = latenciesOverTimeInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyLatenciesOverTime");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 3600000);
    }
    if(isGraph($("#flotLatenciesOverTime"))) {
        infos.createGraph();
    }else {
        var choiceContainer = $("#choicesLatenciesOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotLatenciesOverTime", "#overviewLatenciesOverTime");
        $('#footerLatenciesOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var connectTimeOverTimeInfos = {
        data: {"result": {"minY": 0.0, "minX": 1.73551752E12, "maxY": 4.9E-324, "series": [{"data": [[1.73551782E12, 0.0], [1.73551812E12, 0.0], [1.73551764E12, 0.0], [1.73551794E12, 0.0], [1.73551776E12, 0.0], [1.73551758E12, 0.0], [1.73551806E12, 0.0], [1.73551788E12, 0.0], [1.7355177E12, 0.0], [1.73551752E12, 0.0], [1.735518E12, 0.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551812E12, "title": "Connect Time Over Time"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getConnectTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average Connect Time in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendConnectTimeOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Average connect time was %y ms"
                }
            };
        },
        createGraph: function () {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesConnectTimeOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotConnectTimeOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewConnectTimeOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Connect Time Over Time
function refreshConnectTimeOverTime(fixTimestamps) {
    var infos = connectTimeOverTimeInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyConnectTimeOverTime");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 3600000);
    }
    if(isGraph($("#flotConnectTimeOverTime"))) {
        infos.createGraph();
    }else {
        var choiceContainer = $("#choicesConnectTimeOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotConnectTimeOverTime", "#overviewConnectTimeOverTime");
        $('#footerConnectTimeOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var responseTimePercentilesOverTimeInfos = {
        data: {"result": {"minY": 896.0, "minX": 1.73551752E12, "maxY": 8975.0, "series": [{"data": [[1.73551782E12, 5197.0], [1.73551812E12, 3905.0], [1.73551764E12, 5608.0], [1.73551794E12, 4621.0], [1.73551776E12, 7677.0], [1.73551758E12, 4622.0], [1.73551806E12, 8441.0], [1.73551788E12, 4637.0], [1.7355177E12, 4663.0], [1.73551752E12, 8975.0], [1.735518E12, 7742.0]], "isOverall": false, "label": "Max", "isController": false}, {"data": [[1.73551782E12, 3709.2], [1.73551812E12, 3894.7], [1.73551764E12, 3898.5], [1.73551794E12, 3749.8], [1.73551776E12, 3619.0], [1.73551758E12, 3761.5], [1.73551806E12, 3657.6], [1.73551788E12, 3766.0], [1.7355177E12, 3787.5], [1.73551752E12, 3791.6000000000004], [1.735518E12, 3775.2999999999997]], "isOverall": false, "label": "90th percentile", "isController": false}, {"data": [[1.73551782E12, 4860.699999999998], [1.73551812E12, 3905.0], [1.73551764E12, 5121.839999999997], [1.73551794E12, 4598.21], [1.73551776E12, 7617.6], [1.73551758E12, 4567.41], [1.73551806E12, 8069.889999999998], [1.73551788E12, 4484.240000000002], [1.7355177E12, 4620.649999999999], [1.73551752E12, 7350.5499999999965], [1.735518E12, 5878.18999999999]], "isOverall": false, "label": "99th percentile", "isController": false}, {"data": [[1.73551782E12, 4016.6999999999994], [1.73551812E12, 3905.0], [1.73551764E12, 4124.45], [1.73551794E12, 4026.5], [1.73551776E12, 4056.0], [1.73551758E12, 4196.949999999999], [1.73551806E12, 4035.349999999996], [1.73551788E12, 3945.100000000001], [1.7355177E12, 4080.0], [1.73551752E12, 4161.099999999999], [1.735518E12, 4025.449999999999]], "isOverall": false, "label": "95th percentile", "isController": false}, {"data": [[1.73551782E12, 896.0], [1.73551812E12, 1196.0], [1.73551764E12, 954.0], [1.73551794E12, 1035.0], [1.73551776E12, 926.0], [1.73551758E12, 992.0], [1.73551806E12, 953.0], [1.73551788E12, 996.0], [1.7355177E12, 950.0], [1.73551752E12, 1000.0], [1.735518E12, 904.0]], "isOverall": false, "label": "Min", "isController": false}, {"data": [[1.73551782E12, 2151.5], [1.73551812E12, 1895.0], [1.73551764E12, 1912.5], [1.73551794E12, 2061.0], [1.73551776E12, 1824.0], [1.73551758E12, 1990.5], [1.73551806E12, 1924.5], [1.73551788E12, 2058.0], [1.7355177E12, 2175.0], [1.73551752E12, 2176.5], [1.735518E12, 2091.5]], "isOverall": false, "label": "Median", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551812E12, "title": "Response Time Percentiles Over Time (successful requests only)"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true,
                        fill: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Response Time in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimePercentilesOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Response time was %y ms"
                }
            };
        },
        createGraph: function () {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesResponseTimePercentilesOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimePercentilesOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewResponseTimePercentilesOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Response Time Percentiles Over Time
function refreshResponseTimePercentilesOverTime(fixTimestamps) {
    var infos = responseTimePercentilesOverTimeInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 3600000);
    }
    if(isGraph($("#flotResponseTimePercentilesOverTime"))) {
        infos.createGraph();
    }else {
        var choiceContainer = $("#choicesResponseTimePercentilesOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimePercentilesOverTime", "#overviewResponseTimePercentilesOverTime");
        $('#footerResponseTimePercentilesOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};


var responseTimeVsRequestInfos = {
    data: {"result": {"minY": 1787.5, "minX": 1.0, "maxY": 2530.0, "series": [{"data": [[1.0, 1900.0], [2.0, 1787.5], [4.0, 2212.0], [5.0, 2530.0], [3.0, 1972.0], [6.0, 2498.0]], "isOverall": false, "label": "Successes", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 1000, "maxX": 6.0, "title": "Response Time Vs Request"}},
    getOptions: function() {
        return {
            series: {
                lines: {
                    show: false
                },
                points: {
                    show: true
                }
            },
            xaxis: {
                axisLabel: "Global number of requests per second",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            yaxis: {
                axisLabel: "Median Response Time in ms",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            legend: {
                noColumns: 2,
                show: true,
                container: '#legendResponseTimeVsRequest'
            },
            selection: {
                mode: 'xy'
            },
            grid: {
                hoverable: true // IMPORTANT! this is needed for tooltip to work
            },
            tooltip: true,
            tooltipOpts: {
                content: "%s : Median response time at %x req/s was %y ms"
            },
            colors: ["#9ACD32", "#FF6347"]
        };
    },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesResponseTimeVsRequest"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotResponseTimeVsRequest"), dataset, options);
        // setup overview
        $.plot($("#overviewResponseTimeVsRequest"), dataset, prepareOverviewOptions(options));

    }
};

// Response Time vs Request
function refreshResponseTimeVsRequest() {
    var infos = responseTimeVsRequestInfos;
    prepareSeries(infos.data);
    if (isGraph($("#flotResponseTimeVsRequest"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesResponseTimeVsRequest");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimeVsRequest", "#overviewResponseTimeVsRequest");
        $('#footerResponseRimeVsRequest .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};


var latenciesVsRequestInfos = {
    data: {"result": {"minY": 0.0, "minX": 1.0, "maxY": 4.9E-324, "series": [{"data": [[1.0, 0.0], [2.0, 0.0], [4.0, 0.0], [5.0, 0.0], [3.0, 0.0], [6.0, 0.0]], "isOverall": false, "label": "Successes", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 1000, "maxX": 6.0, "title": "Latencies Vs Request"}},
    getOptions: function() {
        return{
            series: {
                lines: {
                    show: false
                },
                points: {
                    show: true
                }
            },
            xaxis: {
                axisLabel: "Global number of requests per second",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            yaxis: {
                axisLabel: "Median Latency in ms",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            legend: { noColumns: 2,show: true, container: '#legendLatencyVsRequest' },
            selection: {
                mode: 'xy'
            },
            grid: {
                hoverable: true // IMPORTANT! this is needed for tooltip to work
            },
            tooltip: true,
            tooltipOpts: {
                content: "%s : Median Latency time at %x req/s was %y ms"
            },
            colors: ["#9ACD32", "#FF6347"]
        };
    },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesLatencyVsRequest"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotLatenciesVsRequest"), dataset, options);
        // setup overview
        $.plot($("#overviewLatenciesVsRequest"), dataset, prepareOverviewOptions(options));
    }
};

// Latencies vs Request
function refreshLatenciesVsRequest() {
        var infos = latenciesVsRequestInfos;
        prepareSeries(infos.data);
        if(isGraph($("#flotLatenciesVsRequest"))){
            infos.createGraph();
        }else{
            var choiceContainer = $("#choicesLatencyVsRequest");
            createLegend(choiceContainer, infos);
            infos.createGraph();
            setGraphZoomable("#flotLatenciesVsRequest", "#overviewLatenciesVsRequest");
            $('#footerLatenciesVsRequest .legendColorBox > div').each(function(i){
                $(this).clone().prependTo(choiceContainer.find("li").eq(i));
            });
        }
};

var hitsPerSecondInfos = {
        data: {"result": {"minY": 0.05, "minX": 1.73551746E12, "maxY": 2.65, "series": [{"data": [[1.73551782E12, 2.6333333333333333], [1.73551812E12, 0.06666666666666667], [1.73551764E12, 2.6333333333333333], [1.73551746E12, 0.05], [1.73551794E12, 2.533333333333333], [1.73551776E12, 2.65], [1.73551758E12, 2.533333333333333], [1.73551806E12, 2.6333333333333333], [1.73551788E12, 2.6], [1.7355177E12, 2.566666666666667], [1.73551752E12, 2.5833333333333335], [1.735518E12, 2.6333333333333333]], "isOverall": false, "label": "hitsPerSecond", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551812E12, "title": "Hits Per Second"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of hits / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendHitsPerSecond"
                },
                selection: {
                    mode : 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y.2 hits/sec"
                }
            };
        },
        createGraph: function createGraph() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesHitsPerSecond"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotHitsPerSecond"), dataset, options);
            // setup overview
            $.plot($("#overviewHitsPerSecond"), dataset, prepareOverviewOptions(options));
        }
};

// Hits per second
function refreshHitsPerSecond(fixTimestamps) {
    var infos = hitsPerSecondInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 3600000);
    }
    if (isGraph($("#flotHitsPerSecond"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesHitsPerSecond");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotHitsPerSecond", "#overviewHitsPerSecond");
        $('#footerHitsPerSecond .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
}

var codesPerSecondInfos = {
        data: {"result": {"minY": 0.16666666666666666, "minX": 1.73551752E12, "maxY": 2.65, "series": [{"data": [[1.73551782E12, 2.6333333333333333], [1.73551812E12, 0.16666666666666666], [1.73551764E12, 2.6333333333333333], [1.73551794E12, 2.533333333333333], [1.73551776E12, 2.65], [1.73551758E12, 2.533333333333333], [1.73551806E12, 2.6333333333333333], [1.73551788E12, 2.6], [1.7355177E12, 2.566666666666667], [1.73551752E12, 2.533333333333333], [1.735518E12, 2.6333333333333333]], "isOverall": false, "label": "200", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551812E12, "title": "Codes Per Second"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of responses / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendCodesPerSecond"
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "Number of Response Codes %s at %x was %y.2 responses / sec"
                }
            };
        },
    createGraph: function() {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesCodesPerSecond"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotCodesPerSecond"), dataset, options);
        // setup overview
        $.plot($("#overviewCodesPerSecond"), dataset, prepareOverviewOptions(options));
    }
};

// Codes per second
function refreshCodesPerSecond(fixTimestamps) {
    var infos = codesPerSecondInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 3600000);
    }
    if(isGraph($("#flotCodesPerSecond"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesCodesPerSecond");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotCodesPerSecond", "#overviewCodesPerSecond");
        $('#footerCodesPerSecond .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var transactionsPerSecondInfos = {
        data: {"result": {"minY": 0.16666666666666666, "minX": 1.73551752E12, "maxY": 2.65, "series": [{"data": [[1.73551782E12, 2.6333333333333333], [1.73551812E12, 0.16666666666666666], [1.73551764E12, 2.6333333333333333], [1.73551794E12, 2.533333333333333], [1.73551776E12, 2.65], [1.73551758E12, 2.533333333333333], [1.73551806E12, 2.6333333333333333], [1.73551788E12, 2.6], [1.7355177E12, 2.566666666666667], [1.73551752E12, 2.533333333333333], [1.735518E12, 2.6333333333333333]], "isOverall": false, "label": "jp@gc - WebDriver Sampler-success", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551812E12, "title": "Transactions Per Second"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of transactions / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendTransactionsPerSecond"
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y transactions / sec"
                }
            };
        },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesTransactionsPerSecond"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotTransactionsPerSecond"), dataset, options);
        // setup overview
        $.plot($("#overviewTransactionsPerSecond"), dataset, prepareOverviewOptions(options));
    }
};

// Transactions per second
function refreshTransactionsPerSecond(fixTimestamps) {
    var infos = transactionsPerSecondInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyTransactionsPerSecond");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 3600000);
    }
    if(isGraph($("#flotTransactionsPerSecond"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesTransactionsPerSecond");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotTransactionsPerSecond", "#overviewTransactionsPerSecond");
        $('#footerTransactionsPerSecond .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var totalTPSInfos = {
        data: {"result": {"minY": 0.16666666666666666, "minX": 1.73551752E12, "maxY": 2.65, "series": [{"data": [[1.73551782E12, 2.6333333333333333], [1.73551812E12, 0.16666666666666666], [1.73551764E12, 2.6333333333333333], [1.73551794E12, 2.533333333333333], [1.73551776E12, 2.65], [1.73551758E12, 2.533333333333333], [1.73551806E12, 2.6333333333333333], [1.73551788E12, 2.6], [1.7355177E12, 2.566666666666667], [1.73551752E12, 2.533333333333333], [1.735518E12, 2.6333333333333333]], "isOverall": false, "label": "Transaction-success", "isController": false}, {"data": [], "isOverall": false, "label": "Transaction-failure", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551812E12, "title": "Total Transactions Per Second"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of transactions / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendTotalTPS"
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y transactions / sec"
                },
                colors: ["#9ACD32", "#FF6347"]
            };
        },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesTotalTPS"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotTotalTPS"), dataset, options);
        // setup overview
        $.plot($("#overviewTotalTPS"), dataset, prepareOverviewOptions(options));
    }
};

// Total Transactions per second
function refreshTotalTPS(fixTimestamps) {
    var infos = totalTPSInfos;
    // We want to ignore seriesFilter
    prepareSeries(infos.data, false, true);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 3600000);
    }
    if(isGraph($("#flotTotalTPS"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesTotalTPS");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotTotalTPS", "#overviewTotalTPS");
        $('#footerTotalTPS .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

// Collapse the graph matching the specified DOM element depending the collapsed
// status
function collapse(elem, collapsed){
    if(collapsed){
        $(elem).parent().find(".fa-chevron-up").removeClass("fa-chevron-up").addClass("fa-chevron-down");
    } else {
        $(elem).parent().find(".fa-chevron-down").removeClass("fa-chevron-down").addClass("fa-chevron-up");
        if (elem.id == "bodyBytesThroughputOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshBytesThroughputOverTime(true);
            }
            document.location.href="#bytesThroughputOverTime";
        } else if (elem.id == "bodyLatenciesOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshLatenciesOverTime(true);
            }
            document.location.href="#latenciesOverTime";
        } else if (elem.id == "bodyCustomGraph") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshCustomGraph(true);
            }
            document.location.href="#responseCustomGraph";
        } else if (elem.id == "bodyConnectTimeOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshConnectTimeOverTime(true);
            }
            document.location.href="#connectTimeOverTime";
        } else if (elem.id == "bodyResponseTimePercentilesOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshResponseTimePercentilesOverTime(true);
            }
            document.location.href="#responseTimePercentilesOverTime";
        } else if (elem.id == "bodyResponseTimeDistribution") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshResponseTimeDistribution();
            }
            document.location.href="#responseTimeDistribution" ;
        } else if (elem.id == "bodySyntheticResponseTimeDistribution") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshSyntheticResponseTimeDistribution();
            }
            document.location.href="#syntheticResponseTimeDistribution" ;
        } else if (elem.id == "bodyActiveThreadsOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshActiveThreadsOverTime(true);
            }
            document.location.href="#activeThreadsOverTime";
        } else if (elem.id == "bodyTimeVsThreads") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshTimeVsThreads();
            }
            document.location.href="#timeVsThreads" ;
        } else if (elem.id == "bodyCodesPerSecond") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshCodesPerSecond(true);
            }
            document.location.href="#codesPerSecond";
        } else if (elem.id == "bodyTransactionsPerSecond") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshTransactionsPerSecond(true);
            }
            document.location.href="#transactionsPerSecond";
        } else if (elem.id == "bodyTotalTPS") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshTotalTPS(true);
            }
            document.location.href="#totalTPS";
        } else if (elem.id == "bodyResponseTimeVsRequest") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshResponseTimeVsRequest();
            }
            document.location.href="#responseTimeVsRequest";
        } else if (elem.id == "bodyLatenciesVsRequest") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshLatenciesVsRequest();
            }
            document.location.href="#latencyVsRequest";
        }
    }
}

/*
 * Activates or deactivates all series of the specified graph (represented by id parameter)
 * depending on checked argument.
 */
function toggleAll(id, checked){
    var placeholder = document.getElementById(id);

    var cases = $(placeholder).find(':checkbox');
    cases.prop('checked', checked);
    $(cases).parent().children().children().toggleClass("legend-disabled", !checked);

    var choiceContainer;
    if ( id == "choicesBytesThroughputOverTime"){
        choiceContainer = $("#choicesBytesThroughputOverTime");
        refreshBytesThroughputOverTime(false);
    } else if(id == "choicesResponseTimesOverTime"){
        choiceContainer = $("#choicesResponseTimesOverTime");
        refreshResponseTimeOverTime(false);
    }else if(id == "choicesResponseCustomGraph"){
        choiceContainer = $("#choicesResponseCustomGraph");
        refreshCustomGraph(false);
    } else if ( id == "choicesLatenciesOverTime"){
        choiceContainer = $("#choicesLatenciesOverTime");
        refreshLatenciesOverTime(false);
    } else if ( id == "choicesConnectTimeOverTime"){
        choiceContainer = $("#choicesConnectTimeOverTime");
        refreshConnectTimeOverTime(false);
    } else if ( id == "choicesResponseTimePercentilesOverTime"){
        choiceContainer = $("#choicesResponseTimePercentilesOverTime");
        refreshResponseTimePercentilesOverTime(false);
    } else if ( id == "choicesResponseTimePercentiles"){
        choiceContainer = $("#choicesResponseTimePercentiles");
        refreshResponseTimePercentiles();
    } else if(id == "choicesActiveThreadsOverTime"){
        choiceContainer = $("#choicesActiveThreadsOverTime");
        refreshActiveThreadsOverTime(false);
    } else if ( id == "choicesTimeVsThreads"){
        choiceContainer = $("#choicesTimeVsThreads");
        refreshTimeVsThreads();
    } else if ( id == "choicesSyntheticResponseTimeDistribution"){
        choiceContainer = $("#choicesSyntheticResponseTimeDistribution");
        refreshSyntheticResponseTimeDistribution();
    } else if ( id == "choicesResponseTimeDistribution"){
        choiceContainer = $("#choicesResponseTimeDistribution");
        refreshResponseTimeDistribution();
    } else if ( id == "choicesHitsPerSecond"){
        choiceContainer = $("#choicesHitsPerSecond");
        refreshHitsPerSecond(false);
    } else if(id == "choicesCodesPerSecond"){
        choiceContainer = $("#choicesCodesPerSecond");
        refreshCodesPerSecond(false);
    } else if ( id == "choicesTransactionsPerSecond"){
        choiceContainer = $("#choicesTransactionsPerSecond");
        refreshTransactionsPerSecond(false);
    } else if ( id == "choicesTotalTPS"){
        choiceContainer = $("#choicesTotalTPS");
        refreshTotalTPS(false);
    } else if ( id == "choicesResponseTimeVsRequest"){
        choiceContainer = $("#choicesResponseTimeVsRequest");
        refreshResponseTimeVsRequest();
    } else if ( id == "choicesLatencyVsRequest"){
        choiceContainer = $("#choicesLatencyVsRequest");
        refreshLatenciesVsRequest();
    }
    var color = checked ? "black" : "#818181";
    if(choiceContainer != null) {
        choiceContainer.find("label").each(function(){
            this.style.color = color;
        });
    }
}

