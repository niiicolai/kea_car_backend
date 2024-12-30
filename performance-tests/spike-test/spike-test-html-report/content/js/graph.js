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
        data: {"result": {"minY": 1107.0, "minX": 0.0, "maxY": 27421.0, "series": [{"data": [[0.0, 1107.0], [0.1, 1107.0], [0.2, 1107.0], [0.3, 1107.0], [0.4, 1107.0], [0.5, 1107.0], [0.6, 1107.0], [0.7, 1111.0], [0.8, 1111.0], [0.9, 1111.0], [1.0, 1111.0], [1.1, 1111.0], [1.2, 1111.0], [1.3, 1137.0], [1.4, 1137.0], [1.5, 1137.0], [1.6, 1137.0], [1.7, 1137.0], [1.8, 1137.0], [1.9, 1159.0], [2.0, 1159.0], [2.1, 1159.0], [2.2, 1159.0], [2.3, 1159.0], [2.4, 1159.0], [2.5, 1159.0], [2.6, 1165.0], [2.7, 1165.0], [2.8, 1165.0], [2.9, 1165.0], [3.0, 1165.0], [3.1, 1165.0], [3.2, 1186.0], [3.3, 1186.0], [3.4, 1186.0], [3.5, 1186.0], [3.6, 1186.0], [3.7, 1186.0], [3.8, 1186.0], [3.9, 1186.0], [4.0, 1186.0], [4.1, 1186.0], [4.2, 1186.0], [4.3, 1186.0], [4.4, 1186.0], [4.5, 1194.0], [4.6, 1194.0], [4.7, 1194.0], [4.8, 1194.0], [4.9, 1194.0], [5.0, 1194.0], [5.1, 1214.0], [5.2, 1214.0], [5.3, 1214.0], [5.4, 1214.0], [5.5, 1214.0], [5.6, 1214.0], [5.7, 1216.0], [5.8, 1216.0], [5.9, 1216.0], [6.0, 1216.0], [6.1, 1216.0], [6.2, 1216.0], [6.3, 1238.0], [6.4, 1238.0], [6.5, 1238.0], [6.6, 1238.0], [6.7, 1238.0], [6.8, 1238.0], [6.9, 1238.0], [7.0, 1242.0], [7.1, 1242.0], [7.2, 1242.0], [7.3, 1242.0], [7.4, 1242.0], [7.5, 1242.0], [7.6, 1251.0], [7.7, 1251.0], [7.8, 1251.0], [7.9, 1251.0], [8.0, 1251.0], [8.1, 1251.0], [8.2, 1252.0], [8.3, 1252.0], [8.4, 1252.0], [8.5, 1252.0], [8.6, 1252.0], [8.7, 1252.0], [8.8, 1252.0], [8.9, 1256.0], [9.0, 1256.0], [9.1, 1256.0], [9.2, 1256.0], [9.3, 1256.0], [9.4, 1256.0], [9.5, 1256.0], [9.6, 1256.0], [9.7, 1256.0], [9.8, 1256.0], [9.9, 1256.0], [10.0, 1256.0], [10.1, 1257.0], [10.2, 1257.0], [10.3, 1257.0], [10.4, 1257.0], [10.5, 1257.0], [10.6, 1257.0], [10.7, 1258.0], [10.8, 1258.0], [10.9, 1258.0], [11.0, 1258.0], [11.1, 1258.0], [11.2, 1258.0], [11.3, 1258.0], [11.4, 1259.0], [11.5, 1259.0], [11.6, 1259.0], [11.7, 1259.0], [11.8, 1259.0], [11.9, 1259.0], [12.0, 1261.0], [12.1, 1261.0], [12.2, 1261.0], [12.3, 1261.0], [12.4, 1261.0], [12.5, 1261.0], [12.6, 1266.0], [12.7, 1266.0], [12.8, 1266.0], [12.9, 1266.0], [13.0, 1266.0], [13.1, 1266.0], [13.2, 1266.0], [13.3, 1274.0], [13.4, 1274.0], [13.5, 1274.0], [13.6, 1274.0], [13.7, 1274.0], [13.8, 1274.0], [13.9, 1292.0], [14.0, 1292.0], [14.1, 1292.0], [14.2, 1292.0], [14.3, 1292.0], [14.4, 1292.0], [14.5, 1309.0], [14.6, 1309.0], [14.7, 1309.0], [14.8, 1309.0], [14.9, 1309.0], [15.0, 1309.0], [15.1, 1317.0], [15.2, 1317.0], [15.3, 1317.0], [15.4, 1317.0], [15.5, 1317.0], [15.6, 1317.0], [15.7, 1317.0], [15.8, 1324.0], [15.9, 1324.0], [16.0, 1324.0], [16.1, 1324.0], [16.2, 1324.0], [16.3, 1324.0], [16.4, 1328.0], [16.5, 1328.0], [16.6, 1328.0], [16.7, 1328.0], [16.8, 1328.0], [16.9, 1328.0], [17.0, 1330.0], [17.1, 1330.0], [17.2, 1330.0], [17.3, 1330.0], [17.4, 1330.0], [17.5, 1330.0], [17.6, 1330.0], [17.7, 1338.0], [17.8, 1338.0], [17.9, 1338.0], [18.0, 1338.0], [18.1, 1338.0], [18.2, 1338.0], [18.3, 1341.0], [18.4, 1341.0], [18.5, 1341.0], [18.6, 1341.0], [18.7, 1341.0], [18.8, 1341.0], [18.9, 1342.0], [19.0, 1342.0], [19.1, 1342.0], [19.2, 1342.0], [19.3, 1342.0], [19.4, 1342.0], [19.5, 1347.0], [19.6, 1347.0], [19.7, 1347.0], [19.8, 1347.0], [19.9, 1347.0], [20.0, 1347.0], [20.1, 1347.0], [20.2, 1347.0], [20.3, 1347.0], [20.4, 1347.0], [20.5, 1347.0], [20.6, 1347.0], [20.7, 1347.0], [20.8, 1393.0], [20.9, 1393.0], [21.0, 1393.0], [21.1, 1393.0], [21.2, 1393.0], [21.3, 1393.0], [21.4, 1397.0], [21.5, 1397.0], [21.6, 1397.0], [21.7, 1397.0], [21.8, 1397.0], [21.9, 1397.0], [22.0, 1397.0], [22.1, 1399.0], [22.2, 1399.0], [22.3, 1399.0], [22.4, 1399.0], [22.5, 1399.0], [22.6, 1399.0], [22.7, 1433.0], [22.8, 1433.0], [22.9, 1433.0], [23.0, 1433.0], [23.1, 1433.0], [23.2, 1433.0], [23.3, 1508.0], [23.4, 1508.0], [23.5, 1508.0], [23.6, 1508.0], [23.7, 1508.0], [23.8, 1508.0], [23.9, 1630.0], [24.0, 1630.0], [24.1, 1630.0], [24.2, 1630.0], [24.3, 1630.0], [24.4, 1630.0], [24.5, 1630.0], [24.6, 1644.0], [24.7, 1644.0], [24.8, 1644.0], [24.9, 1644.0], [25.0, 1644.0], [25.1, 1644.0], [25.2, 1651.0], [25.3, 1651.0], [25.4, 1651.0], [25.5, 1651.0], [25.6, 1651.0], [25.7, 1651.0], [25.8, 1679.0], [25.9, 1679.0], [26.0, 1679.0], [26.1, 1679.0], [26.2, 1679.0], [26.3, 1679.0], [26.4, 1679.0], [26.5, 1684.0], [26.6, 1684.0], [26.7, 1684.0], [26.8, 1684.0], [26.9, 1684.0], [27.0, 1684.0], [27.1, 1688.0], [27.2, 1688.0], [27.3, 1688.0], [27.4, 1688.0], [27.5, 1688.0], [27.6, 1688.0], [27.7, 1690.0], [27.8, 1690.0], [27.9, 1690.0], [28.0, 1690.0], [28.1, 1690.0], [28.2, 1690.0], [28.3, 1690.0], [28.4, 1733.0], [28.5, 1733.0], [28.6, 1733.0], [28.7, 1733.0], [28.8, 1733.0], [28.9, 1733.0], [29.0, 1751.0], [29.1, 1751.0], [29.2, 1751.0], [29.3, 1751.0], [29.4, 1751.0], [29.5, 1751.0], [29.6, 1766.0], [29.7, 1766.0], [29.8, 1766.0], [29.9, 1766.0], [30.0, 1766.0], [30.1, 1766.0], [30.2, 1778.0], [30.3, 1778.0], [30.4, 1778.0], [30.5, 1778.0], [30.6, 1778.0], [30.7, 1778.0], [30.8, 1778.0], [30.9, 1792.0], [31.0, 1792.0], [31.1, 1792.0], [31.2, 1792.0], [31.3, 1792.0], [31.4, 1792.0], [31.5, 1794.0], [31.6, 1794.0], [31.7, 1794.0], [31.8, 1794.0], [31.9, 1794.0], [32.0, 1794.0], [32.1, 1810.0], [32.2, 1810.0], [32.3, 1810.0], [32.4, 1810.0], [32.5, 1810.0], [32.6, 1810.0], [32.7, 1810.0], [32.8, 1816.0], [32.9, 1816.0], [33.0, 1816.0], [33.1, 1816.0], [33.2, 1816.0], [33.3, 1816.0], [33.4, 1818.0], [33.5, 1818.0], [33.6, 1818.0], [33.7, 1818.0], [33.8, 1818.0], [33.9, 1818.0], [34.0, 1818.0], [34.1, 1818.0], [34.2, 1818.0], [34.3, 1818.0], [34.4, 1818.0], [34.5, 1818.0], [34.6, 1823.0], [34.7, 1823.0], [34.8, 1823.0], [34.9, 1823.0], [35.0, 1823.0], [35.1, 1823.0], [35.2, 1823.0], [35.3, 1860.0], [35.4, 1860.0], [35.5, 1860.0], [35.6, 1860.0], [35.7, 1860.0], [35.8, 1860.0], [35.9, 1875.0], [36.0, 1875.0], [36.1, 1875.0], [36.2, 1875.0], [36.3, 1875.0], [36.4, 1875.0], [36.5, 1881.0], [36.6, 1881.0], [36.7, 1881.0], [36.8, 1881.0], [36.9, 1881.0], [37.0, 1881.0], [37.1, 1881.0], [37.2, 1886.0], [37.3, 1886.0], [37.4, 1886.0], [37.5, 1886.0], [37.6, 1886.0], [37.7, 1886.0], [37.8, 1896.0], [37.9, 1896.0], [38.0, 1896.0], [38.1, 1896.0], [38.2, 1896.0], [38.3, 1896.0], [38.4, 1903.0], [38.5, 1903.0], [38.6, 1903.0], [38.7, 1903.0], [38.8, 1903.0], [38.9, 1903.0], [39.0, 1915.0], [39.1, 1915.0], [39.2, 1915.0], [39.3, 1915.0], [39.4, 1915.0], [39.5, 1915.0], [39.6, 1915.0], [39.7, 1936.0], [39.8, 1936.0], [39.9, 1936.0], [40.0, 1936.0], [40.1, 1936.0], [40.2, 1936.0], [40.3, 1937.0], [40.4, 1937.0], [40.5, 1937.0], [40.6, 1937.0], [40.7, 1937.0], [40.8, 1937.0], [40.9, 1939.0], [41.0, 1939.0], [41.1, 1939.0], [41.2, 1939.0], [41.3, 1939.0], [41.4, 1939.0], [41.5, 1939.0], [41.6, 1962.0], [41.7, 1962.0], [41.8, 1962.0], [41.9, 1962.0], [42.0, 1962.0], [42.1, 1962.0], [42.2, 2005.0], [42.3, 2005.0], [42.4, 2005.0], [42.5, 2005.0], [42.6, 2005.0], [42.7, 2005.0], [42.8, 2005.0], [42.9, 2005.0], [43.0, 2005.0], [43.1, 2005.0], [43.2, 2005.0], [43.3, 2005.0], [43.4, 2066.0], [43.5, 2066.0], [43.6, 2066.0], [43.7, 2066.0], [43.8, 2066.0], [43.9, 2066.0], [44.0, 2066.0], [44.1, 2068.0], [44.2, 2068.0], [44.3, 2068.0], [44.4, 2068.0], [44.5, 2068.0], [44.6, 2068.0], [44.7, 2072.0], [44.8, 2072.0], [44.9, 2072.0], [45.0, 2072.0], [45.1, 2072.0], [45.2, 2072.0], [45.3, 2117.0], [45.4, 2117.0], [45.5, 2117.0], [45.6, 2117.0], [45.7, 2117.0], [45.8, 2117.0], [45.9, 2117.0], [46.0, 2130.0], [46.1, 2130.0], [46.2, 2130.0], [46.3, 2130.0], [46.4, 2130.0], [46.5, 2130.0], [46.6, 2147.0], [46.7, 2147.0], [46.8, 2147.0], [46.9, 2147.0], [47.0, 2147.0], [47.1, 2147.0], [47.2, 2188.0], [47.3, 2188.0], [47.4, 2188.0], [47.5, 2188.0], [47.6, 2188.0], [47.7, 2188.0], [47.8, 2222.0], [47.9, 2222.0], [48.0, 2222.0], [48.1, 2222.0], [48.2, 2222.0], [48.3, 2222.0], [48.4, 2222.0], [48.5, 2282.0], [48.6, 2282.0], [48.7, 2282.0], [48.8, 2282.0], [48.9, 2282.0], [49.0, 2282.0], [49.1, 2349.0], [49.2, 2349.0], [49.3, 2349.0], [49.4, 2349.0], [49.5, 2349.0], [49.6, 2349.0], [49.7, 2354.0], [49.8, 2354.0], [49.9, 2354.0], [50.0, 2354.0], [50.1, 2354.0], [50.2, 2354.0], [50.3, 2354.0], [50.4, 2389.0], [50.5, 2389.0], [50.6, 2389.0], [50.7, 2389.0], [50.8, 2389.0], [50.9, 2389.0], [51.0, 2477.0], [51.1, 2477.0], [51.2, 2477.0], [51.3, 2477.0], [51.4, 2477.0], [51.5, 2477.0], [51.6, 2521.0], [51.7, 2521.0], [51.8, 2521.0], [51.9, 2521.0], [52.0, 2521.0], [52.1, 2521.0], [52.2, 2521.0], [52.3, 2522.0], [52.4, 2522.0], [52.5, 2522.0], [52.6, 2522.0], [52.7, 2522.0], [52.8, 2522.0], [52.9, 2528.0], [53.0, 2528.0], [53.1, 2528.0], [53.2, 2528.0], [53.3, 2528.0], [53.4, 2528.0], [53.5, 2575.0], [53.6, 2575.0], [53.7, 2575.0], [53.8, 2575.0], [53.9, 2575.0], [54.0, 2575.0], [54.1, 2577.0], [54.2, 2577.0], [54.3, 2577.0], [54.4, 2577.0], [54.5, 2577.0], [54.6, 2577.0], [54.7, 2577.0], [54.8, 2598.0], [54.9, 2598.0], [55.0, 2598.0], [55.1, 2598.0], [55.2, 2598.0], [55.3, 2598.0], [55.4, 2620.0], [55.5, 2620.0], [55.6, 2620.0], [55.7, 2620.0], [55.8, 2620.0], [55.9, 2620.0], [56.0, 2625.0], [56.1, 2625.0], [56.2, 2625.0], [56.3, 2625.0], [56.4, 2625.0], [56.5, 2625.0], [56.6, 2625.0], [56.7, 2666.0], [56.8, 2666.0], [56.9, 2666.0], [57.0, 2666.0], [57.1, 2666.0], [57.2, 2666.0], [57.3, 2668.0], [57.4, 2668.0], [57.5, 2668.0], [57.6, 2668.0], [57.7, 2668.0], [57.8, 2668.0], [57.9, 2684.0], [58.0, 2684.0], [58.1, 2684.0], [58.2, 2684.0], [58.3, 2684.0], [58.4, 2684.0], [58.5, 2744.0], [58.6, 2744.0], [58.7, 2744.0], [58.8, 2744.0], [58.9, 2744.0], [59.0, 2744.0], [59.1, 2744.0], [59.2, 2774.0], [59.3, 2774.0], [59.4, 2774.0], [59.5, 2774.0], [59.6, 2774.0], [59.7, 2774.0], [59.8, 2780.0], [59.9, 2780.0], [60.0, 2780.0], [60.1, 2780.0], [60.2, 2780.0], [60.3, 2780.0], [60.4, 2781.0], [60.5, 2781.0], [60.6, 2781.0], [60.7, 2781.0], [60.8, 2781.0], [60.9, 2781.0], [61.0, 2781.0], [61.1, 2833.0], [61.2, 2833.0], [61.3, 2833.0], [61.4, 2833.0], [61.5, 2833.0], [61.6, 2833.0], [61.7, 2851.0], [61.8, 2851.0], [61.9, 2851.0], [62.0, 2851.0], [62.1, 2851.0], [62.2, 2851.0], [62.3, 2854.0], [62.4, 2854.0], [62.5, 2854.0], [62.6, 2854.0], [62.7, 2854.0], [62.8, 2854.0], [62.9, 3324.0], [63.0, 3324.0], [63.1, 3324.0], [63.2, 3324.0], [63.3, 3324.0], [63.4, 3324.0], [63.5, 3324.0], [63.6, 3475.0], [63.7, 3475.0], [63.8, 3475.0], [63.9, 3475.0], [64.0, 3475.0], [64.1, 3475.0], [64.2, 3514.0], [64.3, 3514.0], [64.4, 3514.0], [64.5, 3514.0], [64.6, 3514.0], [64.7, 3514.0], [64.8, 3630.0], [64.9, 3630.0], [65.0, 3630.0], [65.1, 3630.0], [65.2, 3630.0], [65.3, 3630.0], [65.4, 3630.0], [65.5, 3632.0], [65.6, 3632.0], [65.7, 3632.0], [65.8, 3632.0], [65.9, 3632.0], [66.0, 3632.0], [66.1, 3644.0], [66.2, 3644.0], [66.3, 3644.0], [66.4, 3644.0], [66.5, 3644.0], [66.6, 3644.0], [66.7, 3664.0], [66.8, 3664.0], [66.9, 3664.0], [67.0, 3664.0], [67.1, 3664.0], [67.2, 3664.0], [67.3, 3674.0], [67.4, 3674.0], [67.5, 3674.0], [67.6, 3674.0], [67.7, 3674.0], [67.8, 3674.0], [67.9, 3674.0], [68.0, 3694.0], [68.1, 3694.0], [68.2, 3694.0], [68.3, 3694.0], [68.4, 3694.0], [68.5, 3694.0], [68.6, 3700.0], [68.7, 3700.0], [68.8, 3700.0], [68.9, 3700.0], [69.0, 3700.0], [69.1, 3700.0], [69.2, 3721.0], [69.3, 3721.0], [69.4, 3721.0], [69.5, 3721.0], [69.6, 3721.0], [69.7, 3721.0], [69.8, 3721.0], [69.9, 3735.0], [70.0, 3735.0], [70.1, 3735.0], [70.2, 3735.0], [70.3, 3735.0], [70.4, 3735.0], [70.5, 3792.0], [70.6, 3792.0], [70.7, 3792.0], [70.8, 3792.0], [70.9, 3792.0], [71.0, 3792.0], [71.1, 3796.0], [71.2, 3796.0], [71.3, 3796.0], [71.4, 3796.0], [71.5, 3796.0], [71.6, 3796.0], [71.7, 3854.0], [71.8, 3854.0], [71.9, 3854.0], [72.0, 3854.0], [72.1, 3854.0], [72.2, 3854.0], [72.3, 3854.0], [72.4, 3861.0], [72.5, 3861.0], [72.6, 3861.0], [72.7, 3861.0], [72.8, 3861.0], [72.9, 3861.0], [73.0, 3880.0], [73.1, 3880.0], [73.2, 3880.0], [73.3, 3880.0], [73.4, 3880.0], [73.5, 3880.0], [73.6, 3902.0], [73.7, 3902.0], [73.8, 3902.0], [73.9, 3902.0], [74.0, 3902.0], [74.1, 3902.0], [74.2, 3902.0], [74.3, 3989.0], [74.4, 3989.0], [74.5, 3989.0], [74.6, 3989.0], [74.7, 3989.0], [74.8, 3989.0], [74.9, 3994.0], [75.0, 3994.0], [75.1, 3994.0], [75.2, 3994.0], [75.3, 3994.0], [75.4, 3994.0], [75.5, 3997.0], [75.6, 3997.0], [75.7, 3997.0], [75.8, 3997.0], [75.9, 3997.0], [76.0, 3997.0], [76.1, 3997.0], [76.2, 4000.0], [76.3, 4000.0], [76.4, 4000.0], [76.5, 4000.0], [76.6, 4000.0], [76.7, 4000.0], [76.8, 4085.0], [76.9, 4085.0], [77.0, 4085.0], [77.1, 4085.0], [77.2, 4085.0], [77.3, 4085.0], [77.4, 4087.0], [77.5, 4087.0], [77.6, 4087.0], [77.7, 4087.0], [77.8, 4087.0], [77.9, 4087.0], [78.0, 4818.0], [78.1, 4818.0], [78.2, 4818.0], [78.3, 4818.0], [78.4, 4818.0], [78.5, 4818.0], [78.6, 4818.0], [78.7, 5037.0], [78.8, 5037.0], [78.9, 5037.0], [79.0, 5037.0], [79.1, 5037.0], [79.2, 5037.0], [79.3, 5147.0], [79.4, 5147.0], [79.5, 5147.0], [79.6, 5147.0], [79.7, 5147.0], [79.8, 5147.0], [79.9, 5398.0], [80.0, 5398.0], [80.1, 5398.0], [80.2, 5398.0], [80.3, 5398.0], [80.4, 5398.0], [80.5, 5398.0], [80.6, 5420.0], [80.7, 5420.0], [80.8, 5420.0], [80.9, 5420.0], [81.0, 5420.0], [81.1, 5420.0], [81.2, 5832.0], [81.3, 5832.0], [81.4, 5832.0], [81.5, 5832.0], [81.6, 5832.0], [81.7, 5832.0], [81.8, 6000.0], [81.9, 6000.0], [82.0, 6000.0], [82.1, 6000.0], [82.2, 6000.0], [82.3, 6000.0], [82.4, 6041.0], [82.5, 6041.0], [82.6, 6041.0], [82.7, 6041.0], [82.8, 6041.0], [82.9, 6041.0], [83.0, 6041.0], [83.1, 6539.0], [83.2, 6539.0], [83.3, 6539.0], [83.4, 6539.0], [83.5, 6539.0], [83.6, 6539.0], [83.7, 6696.0], [83.8, 6696.0], [83.9, 6696.0], [84.0, 6696.0], [84.1, 6696.0], [84.2, 6696.0], [84.3, 6737.0], [84.4, 6737.0], [84.5, 6737.0], [84.6, 6737.0], [84.7, 6737.0], [84.8, 6737.0], [84.9, 6737.0], [85.0, 8137.0], [85.1, 8137.0], [85.2, 8137.0], [85.3, 8137.0], [85.4, 8137.0], [85.5, 8137.0], [85.6, 8993.0], [85.7, 8993.0], [85.8, 8993.0], [85.9, 8993.0], [86.0, 8993.0], [86.1, 8993.0], [86.2, 9153.0], [86.3, 9153.0], [86.4, 9153.0], [86.5, 9153.0], [86.6, 9153.0], [86.7, 9153.0], [86.8, 9229.0], [86.9, 9229.0], [87.0, 9229.0], [87.1, 9229.0], [87.2, 9229.0], [87.3, 9229.0], [87.4, 9229.0], [87.5, 9412.0], [87.6, 9412.0], [87.7, 9412.0], [87.8, 9412.0], [87.9, 9412.0], [88.0, 9412.0], [88.1, 9779.0], [88.2, 9779.0], [88.3, 9779.0], [88.4, 9779.0], [88.5, 9779.0], [88.6, 9779.0], [88.7, 10224.0], [88.8, 10224.0], [88.9, 10224.0], [89.0, 10224.0], [89.1, 10224.0], [89.2, 10224.0], [89.3, 10224.0], [89.4, 11818.0], [89.5, 11818.0], [89.6, 11818.0], [89.7, 11818.0], [89.8, 11818.0], [89.9, 11818.0], [90.0, 12141.0], [90.1, 12141.0], [90.2, 12141.0], [90.3, 12141.0], [90.4, 12141.0], [90.5, 12141.0], [90.6, 14202.0], [90.7, 14202.0], [90.8, 14202.0], [90.9, 14202.0], [91.0, 14202.0], [91.1, 14202.0], [91.2, 14745.0], [91.3, 14745.0], [91.4, 14745.0], [91.5, 14745.0], [91.6, 14745.0], [91.7, 14745.0], [91.8, 14745.0], [91.9, 16113.0], [92.0, 16113.0], [92.1, 16113.0], [92.2, 16113.0], [92.3, 16113.0], [92.4, 16113.0], [92.5, 16256.0], [92.6, 16256.0], [92.7, 16256.0], [92.8, 16256.0], [92.9, 16256.0], [93.0, 16256.0], [93.1, 17147.0], [93.2, 17147.0], [93.3, 17147.0], [93.4, 17147.0], [93.5, 17147.0], [93.6, 17147.0], [93.7, 17147.0], [93.8, 17818.0], [93.9, 17818.0], [94.0, 17818.0], [94.1, 17818.0], [94.2, 17818.0], [94.3, 17818.0], [94.4, 18654.0], [94.5, 18654.0], [94.6, 18654.0], [94.7, 18654.0], [94.8, 18654.0], [94.9, 18654.0], [95.0, 20471.0], [95.1, 20471.0], [95.2, 20471.0], [95.3, 20471.0], [95.4, 20471.0], [95.5, 20471.0], [95.6, 21097.0], [95.7, 21097.0], [95.8, 21097.0], [95.9, 21097.0], [96.0, 21097.0], [96.1, 21097.0], [96.2, 21097.0], [96.3, 21925.0], [96.4, 21925.0], [96.5, 21925.0], [96.6, 21925.0], [96.7, 21925.0], [96.8, 21925.0], [96.9, 23030.0], [97.0, 23030.0], [97.1, 23030.0], [97.2, 23030.0], [97.3, 23030.0], [97.4, 23030.0], [97.5, 24632.0], [97.6, 24632.0], [97.7, 24632.0], [97.8, 24632.0], [97.9, 24632.0], [98.0, 24632.0], [98.1, 24632.0], [98.2, 24903.0], [98.3, 24903.0], [98.4, 24903.0], [98.5, 24903.0], [98.6, 24903.0], [98.7, 24903.0], [98.8, 27029.0], [98.9, 27029.0], [99.0, 27029.0], [99.1, 27029.0], [99.2, 27029.0], [99.3, 27029.0], [99.4, 27421.0], [99.5, 27421.0], [99.6, 27421.0], [99.7, 27421.0], [99.8, 27421.0], [99.9, 27421.0], [100.0, 27421.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "maxX": 100.0, "title": "Response Time Percentiles"}},
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
        data: {"result": {"minY": 1.0, "minX": 1100.0, "maxY": 15.0, "series": [{"data": [[1100.0, 8.0], [1200.0, 15.0], [1300.0, 13.0], [1400.0, 1.0], [1500.0, 1.0], [1600.0, 7.0], [1700.0, 6.0], [1800.0, 10.0], [1900.0, 6.0], [2000.0, 5.0], [2100.0, 4.0], [2300.0, 3.0], [2200.0, 2.0], [2400.0, 1.0], [2500.0, 6.0], [2600.0, 5.0], [2800.0, 3.0], [2700.0, 4.0], [3300.0, 1.0], [3400.0, 1.0], [3500.0, 1.0], [3700.0, 5.0], [3600.0, 6.0], [3800.0, 3.0], [3900.0, 4.0], [4000.0, 3.0], [4800.0, 1.0], [5100.0, 1.0], [5000.0, 1.0], [5300.0, 1.0], [5400.0, 1.0], [5800.0, 1.0], [6000.0, 2.0], [6600.0, 1.0], [6500.0, 1.0], [6700.0, 1.0], [8100.0, 1.0], [8900.0, 1.0], [9200.0, 1.0], [9100.0, 1.0], [9400.0, 1.0], [9700.0, 1.0], [10200.0, 1.0], [11800.0, 1.0], [12100.0, 1.0], [14200.0, 1.0], [14700.0, 1.0], [16100.0, 1.0], [16200.0, 1.0], [17100.0, 1.0], [17800.0, 1.0], [18600.0, 1.0], [20400.0, 1.0], [21000.0, 1.0], [21900.0, 1.0], [23000.0, 1.0], [24900.0, 1.0], [24600.0, 1.0], [27400.0, 1.0], [27000.0, 1.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 100, "maxX": 27400.0, "title": "Response Time Distribution"}},
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
        data: {"result": {"minY": 25.0, "minX": 1.0, "ticks": [[0, "Requests having \nresponse time <= 500ms"], [1, "Requests having \nresponse time > 500ms and <= 1,500ms"], [2, "Requests having \nresponse time > 1,500ms"], [3, "Requests in error"]], "maxY": 97.0, "series": [{"data": [], "color": "#9ACD32", "isOverall": false, "label": "Requests having \nresponse time <= 500ms", "isController": false}, {"data": [[1.0, 37.0]], "color": "yellow", "isOverall": false, "label": "Requests having \nresponse time > 500ms and <= 1,500ms", "isController": false}, {"data": [[2.0, 97.0]], "color": "orange", "isOverall": false, "label": "Requests having \nresponse time > 1,500ms", "isController": false}, {"data": [[3.0, 25.0]], "color": "#FF6347", "isOverall": false, "label": "Requests in error", "isController": false}], "supportsControllersDiscrimination": false, "maxX": 3.0, "title": "Synthetic Response Times Distribution"}},
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
        data: {"result": {"minY": 1.6666666666666667, "minX": 1.7355144E12, "maxY": 3.260869565217391, "series": [{"data": [[1.7355144E12, 2.0], [1.73551446E12, 2.641509433962265], [1.73551452E12, 1.8333333333333333]], "isOverall": false, "label": "jp@gc - Ultimate Thread Group (Login Test)", "isController": false}, {"data": [[1.7355144E12, 2.0], [1.73551446E12, 2.9142857142857146], [1.73551452E12, 1.8]], "isOverall": false, "label": "jp@gc - Ultimate Thread Group (View Cars Test)", "isController": false}, {"data": [[1.7355144E12, 2.0], [1.73551446E12, 3.260869565217391], [1.73551452E12, 1.6666666666666667]], "isOverall": false, "label": "jp@gc - Ultimate Thread Group (Create Customer Test)", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551452E12, "title": "Active Threads Over Time"}},
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
        data: {"result": {"minY": 1690.0, "minX": 1.0, "maxY": 17701.375000000004, "series": [{"data": [[16.0, 16040.625], [2.0, 1778.0], [1.0, 3324.0], [18.0, 8532.3], [6.0, 2446.706349206348], [12.0, 14668.0], [3.0, 1690.0], [7.0, 15441.5], [15.0, 17701.375000000004]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}, {"data": [[7.723270440251575, 4594.685534591195]], "isOverall": false, "label": "jp@gc - WebDriver Sampler-Aggregated", "isController": false}], "supportsControllersDiscrimination": true, "maxX": 18.0, "title": "Time VS Threads"}},
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
        data : {"result": {"minY": 0.0, "minX": 1.7355144E12, "maxY": 150567.03333333333, "series": [{"data": [[1.7355144E12, 40568.76666666667], [1.73551446E12, 150567.03333333333], [1.73551452E12, 35011.7]], "isOverall": false, "label": "Bytes received per second", "isController": false}, {"data": [[1.7355144E12, 0.0], [1.73551446E12, 0.0], [1.73551452E12, 0.0]], "isOverall": false, "label": "Bytes sent per second", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551452E12, "title": "Bytes Throughput Over Time"}},
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
        data: {"result": {"minY": 2240.142857142857, "minX": 1.7355144E12, "maxY": 5485.315315315315, "series": [{"data": [[1.7355144E12, 2656.5588235294117], [1.73551446E12, 5485.315315315315], [1.73551452E12, 2240.142857142857]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551452E12, "title": "Response Time Over Time"}},
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
        data: {"result": {"minY": 0.0, "minX": 1.7355144E12, "maxY": 4.9E-324, "series": [{"data": [[1.7355144E12, 0.0], [1.73551446E12, 0.0], [1.73551452E12, 0.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551452E12, "title": "Latencies Over Time"}},
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
        data: {"result": {"minY": 0.0, "minX": 1.7355144E12, "maxY": 4.9E-324, "series": [{"data": [[1.7355144E12, 0.0], [1.73551446E12, 0.0], [1.73551452E12, 0.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551452E12, "title": "Connect Time Over Time"}},
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
        data: {"result": {"minY": 1107.0, "minX": 1.7355144E12, "maxY": 9153.0, "series": [{"data": [[1.7355144E12, 6696.0], [1.73551446E12, 9153.0], [1.73551452E12, 4085.0]], "isOverall": false, "label": "Max", "isController": false}, {"data": [[1.7355144E12, 4982.5], [1.73551446E12, 3990.5], [1.73551452E12, 3858.5]], "isOverall": false, "label": "90th percentile", "isController": false}, {"data": [[1.7355144E12, 6696.0], [1.73551446E12, 9153.0], [1.73551452E12, 4085.0]], "isOverall": false, "label": "99th percentile", "isController": false}, {"data": [[1.7355144E12, 6578.25], [1.73551446E12, 5687.7999999999965], [1.73551452E12, 4085.0]], "isOverall": false, "label": "95th percentile", "isController": false}, {"data": [[1.7355144E12, 1111.0], [1.73551446E12, 1107.0], [1.73551452E12, 1186.0]], "isOverall": false, "label": "Min", "isController": false}, {"data": [[1.7355144E12, 2288.0], [1.73551446E12, 1936.5], [1.73551452E12, 1932.5]], "isOverall": false, "label": "Median", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551452E12, "title": "Response Time Percentiles Over Time (successful requests only)"}},
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
    data: {"result": {"minY": 1794.0, "minX": 1.0, "maxY": 16256.0, "series": [{"data": [[2.0, 1794.0], [1.0, 2222.0], [4.0, 2046.0], [5.0, 2744.0], [3.0, 1939.0], [6.0, 2247.0]], "isOverall": false, "label": "Successes", "isController": false}, {"data": [[2.0, 16113.0], [1.0, 16256.0], [3.0, 12141.0]], "isOverall": false, "label": "Failures", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 1000, "maxX": 6.0, "title": "Response Time Vs Request"}},
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
    data: {"result": {"minY": 0.0, "minX": 1.0, "maxY": 4.9E-324, "series": [{"data": [[2.0, 0.0], [1.0, 0.0], [4.0, 0.0], [5.0, 0.0], [3.0, 0.0], [6.0, 0.0]], "isOverall": false, "label": "Successes", "isController": false}, {"data": [[2.0, 0.0], [1.0, 0.0], [3.0, 0.0]], "isOverall": false, "label": "Failures", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 1000, "maxX": 6.0, "title": "Latencies Vs Request"}},
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
        data: {"result": {"minY": 0.13333333333333333, "minX": 1.7355144E12, "maxY": 1.85, "series": [{"data": [[1.7355144E12, 0.6666666666666666], [1.73551446E12, 1.85], [1.73551452E12, 0.13333333333333333]], "isOverall": false, "label": "hitsPerSecond", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551452E12, "title": "Hits Per Second"}},
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
        data: {"result": {"minY": 0.23333333333333334, "minX": 1.7355144E12, "maxY": 1.85, "series": [{"data": [[1.7355144E12, 0.5666666666666667], [1.73551446E12, 1.85], [1.73551452E12, 0.23333333333333334]], "isOverall": false, "label": "200", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551452E12, "title": "Codes Per Second"}},
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
        data: {"result": {"minY": 0.23333333333333334, "minX": 1.7355144E12, "maxY": 1.4333333333333333, "series": [{"data": [[1.73551446E12, 0.4166666666666667]], "isOverall": false, "label": "jp@gc - WebDriver Sampler-failure", "isController": false}, {"data": [[1.7355144E12, 0.5666666666666667], [1.73551446E12, 1.4333333333333333], [1.73551452E12, 0.23333333333333334]], "isOverall": false, "label": "jp@gc - WebDriver Sampler-success", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551452E12, "title": "Transactions Per Second"}},
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
        data: {"result": {"minY": 0.23333333333333334, "minX": 1.7355144E12, "maxY": 1.4333333333333333, "series": [{"data": [[1.7355144E12, 0.5666666666666667], [1.73551446E12, 1.4333333333333333], [1.73551452E12, 0.23333333333333334]], "isOverall": false, "label": "Transaction-success", "isController": false}, {"data": [[1.73551446E12, 0.4166666666666667]], "isOverall": false, "label": "Transaction-failure", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551452E12, "title": "Total Transactions Per Second"}},
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

