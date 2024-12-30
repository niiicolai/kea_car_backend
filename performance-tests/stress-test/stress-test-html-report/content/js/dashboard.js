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
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 27.45098039215686, "KoPercent": 72.54901960784314};
    var dataset = [
        {
            "label" : "FAIL",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "PASS",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.024509803921568627, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [0.024509803921568627, 500, 1500, "jp@gc - WebDriver Sampler"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 102, 74, 72.54901960784314, 22552.352941176454, 996, 77750, 19031.0, 45789.1, 52727.64999999999, 77438.08999999998, 0.8342261734372571, 70.39548492974507, 0.0], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["jp@gc - WebDriver Sampler", 102, 74, 72.54901960784314, 22552.352941176454, 996, 77750, 19031.0, 45789.1, 52727.64999999999, 77438.08999999998, 0.8342261734372571, 70.39548492974507, 0.0], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["The operation lasted too long: It took 18,169 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 42,726 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 11,348 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 40,215 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 32,135 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 33,289 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 38,054 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 32,642 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 43,958 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 28,428 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 19,981 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 18,484 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 25,709 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 10,585 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 77,750 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 15,238 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 57,129 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 24,055 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 27,843 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 40,204 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 13,323 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 16,203 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 10,523 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 41,599 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 32,205 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 32,544 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 29,490 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 44,820 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 48,999 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 29,838 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 18,231 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 49,916 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 45,556 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 28,322 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 33,620 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 15,314 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 34,494 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 6,432 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 41,315 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 13,075 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 53,002 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 7,176 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 30,370 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 9,993 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 24,569 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 45,109 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 25,277 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 20,731 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 12,284 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 46,751 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 19,578 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 35,347 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 51,173 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 11,440 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 43,768 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 34,450 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 67,353 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 24,701 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 24,840 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 18,224 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 10,492 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["500/javax.script.ScriptException: org.openqa.selenium.TimeoutException: Expected condition failed: waiting for url to contain &quot;brands&quot;. Current url: &quot;http://localhost:5173/login&quot; (tried for 30 second(s) with 500 milliseconds interval)\\nBuild info: version: '4.13.0', revision: 'ba948ece5b*'\\nSystem info: os.name: 'Windows 11', os.arch: 'amd64', os.version: '10.0', java.version: '17.0.12'\\nDriver info: org.openqa.selenium.remote.RemoteWebDriver\\nCapabilities {acceptInsecureCerts: false, browserName: chrome, browserVersion: 131.0.6778.205, chrome: {chromedriverVersion: 131.0.6778.204 (52183f9e99a..., userDataDir: C:\\\\Users\\\\niiic\\\\AppData\\\\Loca...}, fedcm:accounts: true, goog:chromeOptions: {debuggerAddress: localhost:55824}, networkConnectionEnabled: false, pageLoadStrategy: normal, platformName: windows, proxy: Proxy(system), setWindowRect: true, strictFileInteractability: false, timeouts: {implicit: 0, pageLoad: 300000, script: 30000}, unhandledPromptBehavior: dismiss and notify, webauthn:extension:credBlob: true, webauthn:extension:largeBlob: true, webauthn:extension:minPinLength: true, webauthn:extension:prf: true, webauthn:virtualAuthenticators: true}\\nSession ID: edb8d302ee8f8a76d94d8f00e3341ae6", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 6,640 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 17,616 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 31,091 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 8,629 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 41,429 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 45,889 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 41,352 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 31,414 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 14,033 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 25,357 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 58,333 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}, {"data": ["The operation lasted too long: It took 18,001 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 1.3513513513513513, 0.9803921568627451], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 102, 74, "The operation lasted too long: It took 18,169 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, "The operation lasted too long: It took 42,726 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, "The operation lasted too long: It took 11,348 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, "The operation lasted too long: It took 40,215 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, "The operation lasted too long: It took 32,135 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": ["jp@gc - WebDriver Sampler", 102, 74, "The operation lasted too long: It took 18,169 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, "The operation lasted too long: It took 42,726 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, "The operation lasted too long: It took 11,348 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, "The operation lasted too long: It took 40,215 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, "The operation lasted too long: It took 32,135 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
