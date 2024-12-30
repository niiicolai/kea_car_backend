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
        data: {"result": {"minY": 996.0, "minX": 0.0, "maxY": 77750.0, "series": [{"data": [[0.0, 996.0], [0.1, 996.0], [0.2, 996.0], [0.3, 996.0], [0.4, 996.0], [0.5, 996.0], [0.6, 996.0], [0.7, 996.0], [0.8, 996.0], [0.9, 996.0], [1.0, 1126.0], [1.1, 1126.0], [1.2, 1126.0], [1.3, 1126.0], [1.4, 1126.0], [1.5, 1126.0], [1.6, 1126.0], [1.7, 1126.0], [1.8, 1126.0], [1.9, 1126.0], [2.0, 1377.0], [2.1, 1377.0], [2.2, 1377.0], [2.3, 1377.0], [2.4, 1377.0], [2.5, 1377.0], [2.6, 1377.0], [2.7, 1377.0], [2.8, 1377.0], [2.9, 1377.0], [3.0, 1449.0], [3.1, 1449.0], [3.2, 1449.0], [3.3, 1449.0], [3.4, 1449.0], [3.5, 1449.0], [3.6, 1449.0], [3.7, 1449.0], [3.8, 1449.0], [3.9, 1449.0], [4.0, 1487.0], [4.1, 1487.0], [4.2, 1487.0], [4.3, 1487.0], [4.4, 1487.0], [4.5, 1487.0], [4.6, 1487.0], [4.7, 1487.0], [4.8, 1487.0], [4.9, 1487.0], [5.0, 1557.0], [5.1, 1557.0], [5.2, 1557.0], [5.3, 1557.0], [5.4, 1557.0], [5.5, 1557.0], [5.6, 1557.0], [5.7, 1557.0], [5.8, 1557.0], [5.9, 1584.0], [6.0, 1584.0], [6.1, 1584.0], [6.2, 1584.0], [6.3, 1584.0], [6.4, 1584.0], [6.5, 1584.0], [6.6, 1584.0], [6.7, 1584.0], [6.8, 1584.0], [6.9, 1611.0], [7.0, 1611.0], [7.1, 1611.0], [7.2, 1611.0], [7.3, 1611.0], [7.4, 1611.0], [7.5, 1611.0], [7.6, 1611.0], [7.7, 1611.0], [7.8, 1611.0], [7.9, 1684.0], [8.0, 1684.0], [8.1, 1684.0], [8.2, 1684.0], [8.3, 1684.0], [8.4, 1684.0], [8.5, 1684.0], [8.6, 1684.0], [8.7, 1684.0], [8.8, 1684.0], [8.9, 1955.0], [9.0, 1955.0], [9.1, 1955.0], [9.2, 1955.0], [9.3, 1955.0], [9.4, 1955.0], [9.5, 1955.0], [9.6, 1955.0], [9.7, 1955.0], [9.8, 1955.0], [9.9, 2410.0], [10.0, 2410.0], [10.1, 2410.0], [10.2, 2410.0], [10.3, 2410.0], [10.4, 2410.0], [10.5, 2410.0], [10.6, 2410.0], [10.7, 2410.0], [10.8, 2427.0], [10.9, 2427.0], [11.0, 2427.0], [11.1, 2427.0], [11.2, 2427.0], [11.3, 2427.0], [11.4, 2427.0], [11.5, 2427.0], [11.6, 2427.0], [11.7, 2427.0], [11.8, 2494.0], [11.9, 2494.0], [12.0, 2494.0], [12.1, 2494.0], [12.2, 2494.0], [12.3, 2494.0], [12.4, 2494.0], [12.5, 2494.0], [12.6, 2494.0], [12.7, 2494.0], [12.8, 2612.0], [12.9, 2612.0], [13.0, 2612.0], [13.1, 2612.0], [13.2, 2612.0], [13.3, 2612.0], [13.4, 2612.0], [13.5, 2612.0], [13.6, 2612.0], [13.7, 2612.0], [13.8, 3013.0], [13.9, 3013.0], [14.0, 3013.0], [14.1, 3013.0], [14.2, 3013.0], [14.3, 3013.0], [14.4, 3013.0], [14.5, 3013.0], [14.6, 3013.0], [14.7, 3013.0], [14.8, 3079.0], [14.9, 3079.0], [15.0, 3079.0], [15.1, 3079.0], [15.2, 3079.0], [15.3, 3079.0], [15.4, 3079.0], [15.5, 3079.0], [15.6, 3079.0], [15.7, 3104.0], [15.8, 3104.0], [15.9, 3104.0], [16.0, 3104.0], [16.1, 3104.0], [16.2, 3104.0], [16.3, 3104.0], [16.4, 3104.0], [16.5, 3104.0], [16.6, 3104.0], [16.7, 3340.0], [16.8, 3340.0], [16.9, 3340.0], [17.0, 3340.0], [17.1, 3340.0], [17.2, 3340.0], [17.3, 3340.0], [17.4, 3340.0], [17.5, 3340.0], [17.6, 3340.0], [17.7, 3609.0], [17.8, 3609.0], [17.9, 3609.0], [18.0, 3609.0], [18.1, 3609.0], [18.2, 3609.0], [18.3, 3609.0], [18.4, 3609.0], [18.5, 3609.0], [18.6, 3609.0], [18.7, 3732.0], [18.8, 3732.0], [18.9, 3732.0], [19.0, 3732.0], [19.1, 3732.0], [19.2, 3732.0], [19.3, 3732.0], [19.4, 3732.0], [19.5, 3732.0], [19.6, 3732.0], [19.7, 3763.0], [19.8, 3763.0], [19.9, 3763.0], [20.0, 3763.0], [20.1, 3763.0], [20.2, 3763.0], [20.3, 3763.0], [20.4, 3763.0], [20.5, 3763.0], [20.6, 4001.0], [20.7, 4001.0], [20.8, 4001.0], [20.9, 4001.0], [21.0, 4001.0], [21.1, 4001.0], [21.2, 4001.0], [21.3, 4001.0], [21.4, 4001.0], [21.5, 4001.0], [21.6, 4383.0], [21.7, 4383.0], [21.8, 4383.0], [21.9, 4383.0], [22.0, 4383.0], [22.1, 4383.0], [22.2, 4383.0], [22.3, 4383.0], [22.4, 4383.0], [22.5, 4383.0], [22.6, 4610.0], [22.7, 4610.0], [22.8, 4610.0], [22.9, 4610.0], [23.0, 4610.0], [23.1, 4610.0], [23.2, 4610.0], [23.3, 4610.0], [23.4, 4610.0], [23.5, 4610.0], [23.6, 4790.0], [23.7, 4790.0], [23.8, 4790.0], [23.9, 4790.0], [24.0, 4790.0], [24.1, 4790.0], [24.2, 4790.0], [24.3, 4790.0], [24.4, 4790.0], [24.5, 4790.0], [24.6, 5012.0], [24.7, 5012.0], [24.8, 5012.0], [24.9, 5012.0], [25.0, 5012.0], [25.1, 5012.0], [25.2, 5012.0], [25.3, 5012.0], [25.4, 5012.0], [25.5, 5324.0], [25.6, 5324.0], [25.7, 5324.0], [25.8, 5324.0], [25.9, 5324.0], [26.0, 5324.0], [26.1, 5324.0], [26.2, 5324.0], [26.3, 5324.0], [26.4, 5324.0], [26.5, 6432.0], [26.6, 6432.0], [26.7, 6432.0], [26.8, 6432.0], [26.9, 6432.0], [27.0, 6432.0], [27.1, 6432.0], [27.2, 6432.0], [27.3, 6432.0], [27.4, 6432.0], [27.5, 6640.0], [27.6, 6640.0], [27.7, 6640.0], [27.8, 6640.0], [27.9, 6640.0], [28.0, 6640.0], [28.1, 6640.0], [28.2, 6640.0], [28.3, 6640.0], [28.4, 6640.0], [28.5, 7176.0], [28.6, 7176.0], [28.7, 7176.0], [28.8, 7176.0], [28.9, 7176.0], [29.0, 7176.0], [29.1, 7176.0], [29.2, 7176.0], [29.3, 7176.0], [29.4, 7176.0], [29.5, 8629.0], [29.6, 8629.0], [29.7, 8629.0], [29.8, 8629.0], [29.9, 8629.0], [30.0, 8629.0], [30.1, 8629.0], [30.2, 8629.0], [30.3, 8629.0], [30.4, 8905.0], [30.5, 8905.0], [30.6, 8905.0], [30.7, 8905.0], [30.8, 8905.0], [30.9, 8905.0], [31.0, 8905.0], [31.1, 8905.0], [31.2, 8905.0], [31.3, 8905.0], [31.4, 9993.0], [31.5, 9993.0], [31.6, 9993.0], [31.7, 9993.0], [31.8, 9993.0], [31.9, 9993.0], [32.0, 9993.0], [32.1, 9993.0], [32.2, 9993.0], [32.3, 9993.0], [32.4, 10492.0], [32.5, 10492.0], [32.6, 10492.0], [32.7, 10492.0], [32.8, 10492.0], [32.9, 10492.0], [33.0, 10492.0], [33.1, 10492.0], [33.2, 10492.0], [33.3, 10492.0], [33.4, 10523.0], [33.5, 10523.0], [33.6, 10523.0], [33.7, 10523.0], [33.8, 10523.0], [33.9, 10523.0], [34.0, 10523.0], [34.1, 10523.0], [34.2, 10523.0], [34.3, 10523.0], [34.4, 10585.0], [34.5, 10585.0], [34.6, 10585.0], [34.7, 10585.0], [34.8, 10585.0], [34.9, 10585.0], [35.0, 10585.0], [35.1, 10585.0], [35.2, 10585.0], [35.3, 11348.0], [35.4, 11348.0], [35.5, 11348.0], [35.6, 11348.0], [35.7, 11348.0], [35.8, 11348.0], [35.9, 11348.0], [36.0, 11348.0], [36.1, 11348.0], [36.2, 11348.0], [36.3, 11440.0], [36.4, 11440.0], [36.5, 11440.0], [36.6, 11440.0], [36.7, 11440.0], [36.8, 11440.0], [36.9, 11440.0], [37.0, 11440.0], [37.1, 11440.0], [37.2, 11440.0], [37.3, 12284.0], [37.4, 12284.0], [37.5, 12284.0], [37.6, 12284.0], [37.7, 12284.0], [37.8, 12284.0], [37.9, 12284.0], [38.0, 12284.0], [38.1, 12284.0], [38.2, 12284.0], [38.3, 13075.0], [38.4, 13075.0], [38.5, 13075.0], [38.6, 13075.0], [38.7, 13075.0], [38.8, 13075.0], [38.9, 13075.0], [39.0, 13075.0], [39.1, 13075.0], [39.2, 13075.0], [39.3, 13323.0], [39.4, 13323.0], [39.5, 13323.0], [39.6, 13323.0], [39.7, 13323.0], [39.8, 13323.0], [39.9, 13323.0], [40.0, 13323.0], [40.1, 13323.0], [40.2, 14033.0], [40.3, 14033.0], [40.4, 14033.0], [40.5, 14033.0], [40.6, 14033.0], [40.7, 14033.0], [40.8, 14033.0], [40.9, 14033.0], [41.0, 14033.0], [41.1, 14033.0], [41.2, 15238.0], [41.3, 15238.0], [41.4, 15238.0], [41.5, 15238.0], [41.6, 15238.0], [41.7, 15238.0], [41.8, 15238.0], [41.9, 15238.0], [42.0, 15238.0], [42.1, 15238.0], [42.2, 15314.0], [42.3, 15314.0], [42.4, 15314.0], [42.5, 15314.0], [42.6, 15314.0], [42.7, 15314.0], [42.8, 15314.0], [42.9, 15314.0], [43.0, 15314.0], [43.1, 15314.0], [43.2, 16203.0], [43.3, 16203.0], [43.4, 16203.0], [43.5, 16203.0], [43.6, 16203.0], [43.7, 16203.0], [43.8, 16203.0], [43.9, 16203.0], [44.0, 16203.0], [44.1, 16203.0], [44.2, 17616.0], [44.3, 17616.0], [44.4, 17616.0], [44.5, 17616.0], [44.6, 17616.0], [44.7, 17616.0], [44.8, 17616.0], [44.9, 17616.0], [45.0, 17616.0], [45.1, 18001.0], [45.2, 18001.0], [45.3, 18001.0], [45.4, 18001.0], [45.5, 18001.0], [45.6, 18001.0], [45.7, 18001.0], [45.8, 18001.0], [45.9, 18001.0], [46.0, 18001.0], [46.1, 18169.0], [46.2, 18169.0], [46.3, 18169.0], [46.4, 18169.0], [46.5, 18169.0], [46.6, 18169.0], [46.7, 18169.0], [46.8, 18169.0], [46.9, 18169.0], [47.0, 18169.0], [47.1, 18224.0], [47.2, 18224.0], [47.3, 18224.0], [47.4, 18224.0], [47.5, 18224.0], [47.6, 18224.0], [47.7, 18224.0], [47.8, 18224.0], [47.9, 18224.0], [48.0, 18224.0], [48.1, 18231.0], [48.2, 18231.0], [48.3, 18231.0], [48.4, 18231.0], [48.5, 18231.0], [48.6, 18231.0], [48.7, 18231.0], [48.8, 18231.0], [48.9, 18231.0], [49.0, 18231.0], [49.1, 18484.0], [49.2, 18484.0], [49.3, 18484.0], [49.4, 18484.0], [49.5, 18484.0], [49.6, 18484.0], [49.7, 18484.0], [49.8, 18484.0], [49.9, 18484.0], [50.0, 19578.0], [50.1, 19578.0], [50.2, 19578.0], [50.3, 19578.0], [50.4, 19578.0], [50.5, 19578.0], [50.6, 19578.0], [50.7, 19578.0], [50.8, 19578.0], [50.9, 19578.0], [51.0, 19981.0], [51.1, 19981.0], [51.2, 19981.0], [51.3, 19981.0], [51.4, 19981.0], [51.5, 19981.0], [51.6, 19981.0], [51.7, 19981.0], [51.8, 19981.0], [51.9, 19981.0], [52.0, 20731.0], [52.1, 20731.0], [52.2, 20731.0], [52.3, 20731.0], [52.4, 20731.0], [52.5, 20731.0], [52.6, 20731.0], [52.7, 20731.0], [52.8, 20731.0], [52.9, 20731.0], [53.0, 24055.0], [53.1, 24055.0], [53.2, 24055.0], [53.3, 24055.0], [53.4, 24055.0], [53.5, 24055.0], [53.6, 24055.0], [53.7, 24055.0], [53.8, 24055.0], [53.9, 24055.0], [54.0, 24569.0], [54.1, 24569.0], [54.2, 24569.0], [54.3, 24569.0], [54.4, 24569.0], [54.5, 24569.0], [54.6, 24569.0], [54.7, 24569.0], [54.8, 24569.0], [54.9, 24569.0], [55.0, 24701.0], [55.1, 24701.0], [55.2, 24701.0], [55.3, 24701.0], [55.4, 24701.0], [55.5, 24701.0], [55.6, 24701.0], [55.7, 24701.0], [55.8, 24701.0], [55.9, 24840.0], [56.0, 24840.0], [56.1, 24840.0], [56.2, 24840.0], [56.3, 24840.0], [56.4, 24840.0], [56.5, 24840.0], [56.6, 24840.0], [56.7, 24840.0], [56.8, 24840.0], [56.9, 25277.0], [57.0, 25277.0], [57.1, 25277.0], [57.2, 25277.0], [57.3, 25277.0], [57.4, 25277.0], [57.5, 25277.0], [57.6, 25277.0], [57.7, 25277.0], [57.8, 25277.0], [57.9, 25357.0], [58.0, 25357.0], [58.1, 25357.0], [58.2, 25357.0], [58.3, 25357.0], [58.4, 25357.0], [58.5, 25357.0], [58.6, 25357.0], [58.7, 25357.0], [58.8, 25357.0], [58.9, 25709.0], [59.0, 25709.0], [59.1, 25709.0], [59.2, 25709.0], [59.3, 25709.0], [59.4, 25709.0], [59.5, 25709.0], [59.6, 25709.0], [59.7, 25709.0], [59.8, 25709.0], [59.9, 27843.0], [60.0, 27843.0], [60.1, 27843.0], [60.2, 27843.0], [60.3, 27843.0], [60.4, 27843.0], [60.5, 27843.0], [60.6, 27843.0], [60.7, 27843.0], [60.8, 28322.0], [60.9, 28322.0], [61.0, 28322.0], [61.1, 28322.0], [61.2, 28322.0], [61.3, 28322.0], [61.4, 28322.0], [61.5, 28322.0], [61.6, 28322.0], [61.7, 28322.0], [61.8, 28428.0], [61.9, 28428.0], [62.0, 28428.0], [62.1, 28428.0], [62.2, 28428.0], [62.3, 28428.0], [62.4, 28428.0], [62.5, 28428.0], [62.6, 28428.0], [62.7, 28428.0], [62.8, 29490.0], [62.9, 29490.0], [63.0, 29490.0], [63.1, 29490.0], [63.2, 29490.0], [63.3, 29490.0], [63.4, 29490.0], [63.5, 29490.0], [63.6, 29490.0], [63.7, 29490.0], [63.8, 29838.0], [63.9, 29838.0], [64.0, 29838.0], [64.1, 29838.0], [64.2, 29838.0], [64.3, 29838.0], [64.4, 29838.0], [64.5, 29838.0], [64.6, 29838.0], [64.7, 29838.0], [64.8, 30370.0], [64.9, 30370.0], [65.0, 30370.0], [65.1, 30370.0], [65.2, 30370.0], [65.3, 30370.0], [65.4, 30370.0], [65.5, 30370.0], [65.6, 30370.0], [65.7, 31091.0], [65.8, 31091.0], [65.9, 31091.0], [66.0, 31091.0], [66.1, 31091.0], [66.2, 31091.0], [66.3, 31091.0], [66.4, 31091.0], [66.5, 31091.0], [66.6, 31091.0], [66.7, 31414.0], [66.8, 31414.0], [66.9, 31414.0], [67.0, 31414.0], [67.1, 31414.0], [67.2, 31414.0], [67.3, 31414.0], [67.4, 31414.0], [67.5, 31414.0], [67.6, 31414.0], [67.7, 32135.0], [67.8, 32135.0], [67.9, 32135.0], [68.0, 32135.0], [68.1, 32135.0], [68.2, 32135.0], [68.3, 32135.0], [68.4, 32135.0], [68.5, 32135.0], [68.6, 32135.0], [68.7, 32205.0], [68.8, 32205.0], [68.9, 32205.0], [69.0, 32205.0], [69.1, 32205.0], [69.2, 32205.0], [69.3, 32205.0], [69.4, 32205.0], [69.5, 32205.0], [69.6, 32205.0], [69.7, 32544.0], [69.8, 32544.0], [69.9, 32544.0], [70.0, 32544.0], [70.1, 32544.0], [70.2, 32544.0], [70.3, 32544.0], [70.4, 32544.0], [70.5, 32544.0], [70.6, 32642.0], [70.7, 32642.0], [70.8, 32642.0], [70.9, 32642.0], [71.0, 32642.0], [71.1, 32642.0], [71.2, 32642.0], [71.3, 32642.0], [71.4, 32642.0], [71.5, 32642.0], [71.6, 33289.0], [71.7, 33289.0], [71.8, 33289.0], [71.9, 33289.0], [72.0, 33289.0], [72.1, 33289.0], [72.2, 33289.0], [72.3, 33289.0], [72.4, 33289.0], [72.5, 33289.0], [72.6, 33620.0], [72.7, 33620.0], [72.8, 33620.0], [72.9, 33620.0], [73.0, 33620.0], [73.1, 33620.0], [73.2, 33620.0], [73.3, 33620.0], [73.4, 33620.0], [73.5, 33620.0], [73.6, 34450.0], [73.7, 34450.0], [73.8, 34450.0], [73.9, 34450.0], [74.0, 34450.0], [74.1, 34450.0], [74.2, 34450.0], [74.3, 34450.0], [74.4, 34450.0], [74.5, 34450.0], [74.6, 34494.0], [74.7, 34494.0], [74.8, 34494.0], [74.9, 34494.0], [75.0, 34494.0], [75.1, 34494.0], [75.2, 34494.0], [75.3, 34494.0], [75.4, 34494.0], [75.5, 34733.0], [75.6, 34733.0], [75.7, 34733.0], [75.8, 34733.0], [75.9, 34733.0], [76.0, 34733.0], [76.1, 34733.0], [76.2, 34733.0], [76.3, 34733.0], [76.4, 34733.0], [76.5, 35347.0], [76.6, 35347.0], [76.7, 35347.0], [76.8, 35347.0], [76.9, 35347.0], [77.0, 35347.0], [77.1, 35347.0], [77.2, 35347.0], [77.3, 35347.0], [77.4, 35347.0], [77.5, 38054.0], [77.6, 38054.0], [77.7, 38054.0], [77.8, 38054.0], [77.9, 38054.0], [78.0, 38054.0], [78.1, 38054.0], [78.2, 38054.0], [78.3, 38054.0], [78.4, 38054.0], [78.5, 40204.0], [78.6, 40204.0], [78.7, 40204.0], [78.8, 40204.0], [78.9, 40204.0], [79.0, 40204.0], [79.1, 40204.0], [79.2, 40204.0], [79.3, 40204.0], [79.4, 40204.0], [79.5, 40215.0], [79.6, 40215.0], [79.7, 40215.0], [79.8, 40215.0], [79.9, 40215.0], [80.0, 40215.0], [80.1, 40215.0], [80.2, 40215.0], [80.3, 40215.0], [80.4, 41315.0], [80.5, 41315.0], [80.6, 41315.0], [80.7, 41315.0], [80.8, 41315.0], [80.9, 41315.0], [81.0, 41315.0], [81.1, 41315.0], [81.2, 41315.0], [81.3, 41315.0], [81.4, 41352.0], [81.5, 41352.0], [81.6, 41352.0], [81.7, 41352.0], [81.8, 41352.0], [81.9, 41352.0], [82.0, 41352.0], [82.1, 41352.0], [82.2, 41352.0], [82.3, 41352.0], [82.4, 41429.0], [82.5, 41429.0], [82.6, 41429.0], [82.7, 41429.0], [82.8, 41429.0], [82.9, 41429.0], [83.0, 41429.0], [83.1, 41429.0], [83.2, 41429.0], [83.3, 41429.0], [83.4, 41599.0], [83.5, 41599.0], [83.6, 41599.0], [83.7, 41599.0], [83.8, 41599.0], [83.9, 41599.0], [84.0, 41599.0], [84.1, 41599.0], [84.2, 41599.0], [84.3, 41599.0], [84.4, 42726.0], [84.5, 42726.0], [84.6, 42726.0], [84.7, 42726.0], [84.8, 42726.0], [84.9, 42726.0], [85.0, 42726.0], [85.1, 42726.0], [85.2, 42726.0], [85.3, 43768.0], [85.4, 43768.0], [85.5, 43768.0], [85.6, 43768.0], [85.7, 43768.0], [85.8, 43768.0], [85.9, 43768.0], [86.0, 43768.0], [86.1, 43768.0], [86.2, 43768.0], [86.3, 43958.0], [86.4, 43958.0], [86.5, 43958.0], [86.6, 43958.0], [86.7, 43958.0], [86.8, 43958.0], [86.9, 43958.0], [87.0, 43958.0], [87.1, 43958.0], [87.2, 43958.0], [87.3, 44820.0], [87.4, 44820.0], [87.5, 44820.0], [87.6, 44820.0], [87.7, 44820.0], [87.8, 44820.0], [87.9, 44820.0], [88.0, 44820.0], [88.1, 44820.0], [88.2, 44820.0], [88.3, 45109.0], [88.4, 45109.0], [88.5, 45109.0], [88.6, 45109.0], [88.7, 45109.0], [88.8, 45109.0], [88.9, 45109.0], [89.0, 45109.0], [89.1, 45109.0], [89.2, 45109.0], [89.3, 45556.0], [89.4, 45556.0], [89.5, 45556.0], [89.6, 45556.0], [89.7, 45556.0], [89.8, 45556.0], [89.9, 45556.0], [90.0, 45556.0], [90.1, 45556.0], [90.2, 45889.0], [90.3, 45889.0], [90.4, 45889.0], [90.5, 45889.0], [90.6, 45889.0], [90.7, 45889.0], [90.8, 45889.0], [90.9, 45889.0], [91.0, 45889.0], [91.1, 45889.0], [91.2, 46751.0], [91.3, 46751.0], [91.4, 46751.0], [91.5, 46751.0], [91.6, 46751.0], [91.7, 46751.0], [91.8, 46751.0], [91.9, 46751.0], [92.0, 46751.0], [92.1, 46751.0], [92.2, 48999.0], [92.3, 48999.0], [92.4, 48999.0], [92.5, 48999.0], [92.6, 48999.0], [92.7, 48999.0], [92.8, 48999.0], [92.9, 48999.0], [93.0, 48999.0], [93.1, 48999.0], [93.2, 49916.0], [93.3, 49916.0], [93.4, 49916.0], [93.5, 49916.0], [93.6, 49916.0], [93.7, 49916.0], [93.8, 49916.0], [93.9, 49916.0], [94.0, 49916.0], [94.1, 49916.0], [94.2, 51173.0], [94.3, 51173.0], [94.4, 51173.0], [94.5, 51173.0], [94.6, 51173.0], [94.7, 51173.0], [94.8, 51173.0], [94.9, 51173.0], [95.0, 51173.0], [95.1, 53002.0], [95.2, 53002.0], [95.3, 53002.0], [95.4, 53002.0], [95.5, 53002.0], [95.6, 53002.0], [95.7, 53002.0], [95.8, 53002.0], [95.9, 53002.0], [96.0, 53002.0], [96.1, 57129.0], [96.2, 57129.0], [96.3, 57129.0], [96.4, 57129.0], [96.5, 57129.0], [96.6, 57129.0], [96.7, 57129.0], [96.8, 57129.0], [96.9, 57129.0], [97.0, 57129.0], [97.1, 58333.0], [97.2, 58333.0], [97.3, 58333.0], [97.4, 58333.0], [97.5, 58333.0], [97.6, 58333.0], [97.7, 58333.0], [97.8, 58333.0], [97.9, 58333.0], [98.0, 58333.0], [98.1, 67353.0], [98.2, 67353.0], [98.3, 67353.0], [98.4, 67353.0], [98.5, 67353.0], [98.6, 67353.0], [98.7, 67353.0], [98.8, 67353.0], [98.9, 67353.0], [99.0, 67353.0], [99.1, 77750.0], [99.2, 77750.0], [99.3, 77750.0], [99.4, 77750.0], [99.5, 77750.0], [99.6, 77750.0], [99.7, 77750.0], [99.8, 77750.0], [99.9, 77750.0], [100.0, 77750.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "maxX": 100.0, "title": "Response Time Percentiles"}},
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
        data: {"result": {"minY": 1.0, "minX": 900.0, "maxY": 3.0, "series": [{"data": [[900.0, 1.0], [1100.0, 1.0], [1300.0, 1.0], [1400.0, 2.0], [1500.0, 2.0], [1600.0, 2.0], [1900.0, 1.0], [2400.0, 3.0], [2600.0, 1.0], [3000.0, 2.0], [3100.0, 1.0], [3300.0, 1.0], [3700.0, 2.0], [3600.0, 1.0], [4000.0, 1.0], [4300.0, 1.0], [67300.0, 1.0], [4600.0, 1.0], [4700.0, 1.0], [77700.0, 1.0], [5000.0, 1.0], [5300.0, 1.0], [6400.0, 1.0], [6600.0, 1.0], [7100.0, 1.0], [8600.0, 1.0], [8900.0, 1.0], [9900.0, 1.0], [10500.0, 2.0], [10400.0, 1.0], [11400.0, 1.0], [11300.0, 1.0], [12200.0, 1.0], [13000.0, 1.0], [13300.0, 1.0], [14000.0, 1.0], [15300.0, 1.0], [15200.0, 1.0], [16200.0, 1.0], [18000.0, 1.0], [18400.0, 1.0], [18100.0, 1.0], [18200.0, 2.0], [17600.0, 1.0], [19500.0, 1.0], [19900.0, 1.0], [20700.0, 1.0], [24500.0, 1.0], [24000.0, 1.0], [25300.0, 1.0], [25200.0, 1.0], [24700.0, 1.0], [24800.0, 1.0], [25700.0, 1.0], [27800.0, 1.0], [28300.0, 1.0], [28400.0, 1.0], [29400.0, 1.0], [29800.0, 1.0], [30300.0, 1.0], [31000.0, 1.0], [31400.0, 1.0], [32500.0, 1.0], [32600.0, 1.0], [32100.0, 1.0], [32200.0, 1.0], [34400.0, 2.0], [33200.0, 1.0], [33600.0, 1.0], [34700.0, 1.0], [35300.0, 1.0], [38000.0, 1.0], [40200.0, 2.0], [41500.0, 1.0], [41300.0, 2.0], [42700.0, 1.0], [41400.0, 1.0], [44800.0, 1.0], [43700.0, 1.0], [43900.0, 1.0], [46700.0, 1.0], [45100.0, 1.0], [45800.0, 1.0], [45500.0, 1.0], [48900.0, 1.0], [51100.0, 1.0], [49900.0, 1.0], [53000.0, 1.0], [57100.0, 1.0], [58300.0, 1.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 100, "maxX": 77700.0, "title": "Response Time Distribution"}},
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
        data: {"result": {"minY": 5.0, "minX": 1.0, "ticks": [[0, "Requests having \nresponse time <= 500ms"], [1, "Requests having \nresponse time > 500ms and <= 1,500ms"], [2, "Requests having \nresponse time > 1,500ms"], [3, "Requests in error"]], "maxY": 74.0, "series": [{"data": [], "color": "#9ACD32", "isOverall": false, "label": "Requests having \nresponse time <= 500ms", "isController": false}, {"data": [[1.0, 5.0]], "color": "yellow", "isOverall": false, "label": "Requests having \nresponse time > 500ms and <= 1,500ms", "isController": false}, {"data": [[2.0, 23.0]], "color": "orange", "isOverall": false, "label": "Requests having \nresponse time > 1,500ms", "isController": false}, {"data": [[3.0, 74.0]], "color": "#FF6347", "isOverall": false, "label": "Requests in error", "isController": false}], "supportsControllersDiscrimination": false, "maxX": 3.0, "title": "Synthetic Response Times Distribution"}},
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
        data: {"result": {"minY": 2.727272727272727, "minX": 1.73551176E12, "maxY": 7.636363636363636, "series": [{"data": [[1.73551188E12, 5.916666666666666], [1.73551176E12, 3.0], [1.73551182E12, 7.428571428571429]], "isOverall": false, "label": "jp@gc - Stepping Thread Group (Create Customer Test)", "isController": false}, {"data": [[1.73551188E12, 6.6], [1.73551176E12, 2.727272727272727], [1.73551182E12, 7.636363636363636]], "isOverall": false, "label": "jp@gc - Stepping Thread Group (View Cars Test)", "isController": false}, {"data": [[1.73551188E12, 6.8], [1.73551176E12, 2.764705882352941], [1.73551182E12, 7.473684210526316]], "isOverall": false, "label": "jp@gc - Stepping Thread Group (Login Test)", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551188E12, "title": "Active Threads Over Time"}},
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
        data: {"result": {"minY": 1907.0, "minX": 2.0, "maxY": 44097.6, "series": [{"data": [[2.0, 21532.0], [9.0, 3723.4], [3.0, 1907.0], [12.0, 14092.75], [14.0, 7176.0], [15.0, 17731.600000000002], [4.0, 40451.5], [17.0, 44097.6], [18.0, 36696.75], [5.0, 24701.0], [21.0, 16071.2], [6.0, 2559.9090909090905], [24.0, 32813.92682926829], [7.0, 22393.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}, {"data": [[16.245098039215684, 22552.352941176454]], "isOverall": false, "label": "jp@gc - WebDriver Sampler-Aggregated", "isController": false}], "supportsControllersDiscrimination": true, "maxX": 24.0, "title": "Time VS Threads"}},
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
        data : {"result": {"minY": 0.0, "minX": 1.73551176E12, "maxY": 67724.36666666667, "series": [{"data": [[1.73551188E12, 37575.26666666667], [1.73551176E12, 67724.36666666667], [1.73551182E12, 41596.333333333336]], "isOverall": false, "label": "Bytes received per second", "isController": false}, {"data": [[1.73551188E12, 0.0], [1.73551176E12, 0.0], [1.73551182E12, 0.0]], "isOverall": false, "label": "Bytes sent per second", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551188E12, "title": "Bytes Throughput Over Time"}},
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
        data: {"result": {"minY": 3893.030303030302, "minX": 1.73551176E12, "maxY": 39223.9375, "series": [{"data": [[1.73551188E12, 39223.9375], [1.73551176E12, 3893.030303030302], [1.73551182E12, 24775.783783783783]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551188E12, "title": "Response Time Over Time"}},
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
        data: {"result": {"minY": 0.0, "minX": 1.73551176E12, "maxY": 4.9E-324, "series": [{"data": [[1.73551188E12, 0.0], [1.73551176E12, 0.0], [1.73551182E12, 0.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551188E12, "title": "Latencies Over Time"}},
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
        data: {"result": {"minY": 0.0, "minX": 1.73551176E12, "maxY": 4.9E-324, "series": [{"data": [[1.73551188E12, 0.0], [1.73551176E12, 0.0], [1.73551182E12, 0.0]], "isOverall": false, "label": "jp@gc - WebDriver Sampler", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551188E12, "title": "Connect Time Over Time"}},
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
        data: {"result": {"minY": 996.0, "minX": 1.73551176E12, "maxY": 8905.0, "series": [{"data": [[1.73551176E12, 8905.0]], "isOverall": false, "label": "Max", "isController": false}, {"data": [[1.73551176E12, 5043.200000000001]], "isOverall": false, "label": "90th percentile", "isController": false}, {"data": [[1.73551176E12, 8905.0]], "isOverall": false, "label": "99th percentile", "isController": false}, {"data": [[1.73551176E12, 7293.54999999999]], "isOverall": false, "label": "95th percentile", "isController": false}, {"data": [[1.73551176E12, 996.0]], "isOverall": false, "label": "Min", "isController": false}, {"data": [[1.73551176E12, 2812.5]], "isOverall": false, "label": "Median", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551176E12, "title": "Response Time Percentiles Over Time (successful requests only)"}},
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
    data: {"result": {"minY": 1955.0, "minX": 1.0, "maxY": 43958.0, "series": [{"data": [[1.0, 3013.0], [2.0, 2047.0], [4.0, 4310.5], [5.0, 1955.0]], "isOverall": false, "label": "Successes", "isController": false}, {"data": [[2.0, 24704.5], [1.0, 28322.0], [4.0, 41858.5], [5.0, 24701.0], [3.0, 28428.0], [7.0, 43958.0]], "isOverall": false, "label": "Failures", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 1000, "maxX": 7.0, "title": "Response Time Vs Request"}},
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
    data: {"result": {"minY": 0.0, "minX": 1.0, "maxY": 4.9E-324, "series": [{"data": [[1.0, 0.0], [2.0, 0.0], [4.0, 0.0], [5.0, 0.0]], "isOverall": false, "label": "Successes", "isController": false}, {"data": [[2.0, 0.0], [1.0, 0.0], [4.0, 0.0], [5.0, 0.0], [3.0, 0.0], [7.0, 0.0]], "isOverall": false, "label": "Failures", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 1000, "maxX": 7.0, "title": "Latencies Vs Request"}},
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
        data: {"result": {"minY": 0.15, "minX": 1.73551176E12, "maxY": 0.8, "series": [{"data": [[1.73551188E12, 0.15], [1.73551176E12, 0.8], [1.73551182E12, 0.75]], "isOverall": false, "label": "hitsPerSecond", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551188E12, "title": "Hits Per Second"}},
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
        data: {"result": {"minY": 0.016666666666666666, "minX": 1.73551176E12, "maxY": 0.6166666666666667, "series": [{"data": [[1.73551188E12, 0.5166666666666667], [1.73551176E12, 0.55], [1.73551182E12, 0.6166666666666667]], "isOverall": false, "label": "200", "isController": false}, {"data": [[1.73551188E12, 0.016666666666666666]], "isOverall": false, "label": "500", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.73551188E12, "title": "Codes Per Second"}},
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
        data: {"result": {"minY": 0.08333333333333333, "minX": 1.73551176E12, "maxY": 0.6166666666666667, "series": [{"data": [[1.73551188E12, 0.5333333333333333], [1.73551176E12, 0.08333333333333333], [1.73551182E12, 0.6166666666666667]], "isOverall": false, "label": "jp@gc - WebDriver Sampler-failure", "isController": false}, {"data": [[1.73551176E12, 0.4666666666666667]], "isOverall": false, "label": "jp@gc - WebDriver Sampler-success", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551188E12, "title": "Transactions Per Second"}},
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
        data: {"result": {"minY": 0.08333333333333333, "minX": 1.73551176E12, "maxY": 0.6166666666666667, "series": [{"data": [[1.73551176E12, 0.4666666666666667]], "isOverall": false, "label": "Transaction-success", "isController": false}, {"data": [[1.73551188E12, 0.5333333333333333], [1.73551176E12, 0.08333333333333333], [1.73551182E12, 0.6166666666666667]], "isOverall": false, "label": "Transaction-failure", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.73551188E12, "title": "Total Transactions Per Second"}},
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

