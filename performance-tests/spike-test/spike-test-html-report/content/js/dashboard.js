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

    var data = {"OkPercent": 84.27672955974843, "KoPercent": 15.723270440251572};
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
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.11635220125786164, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [0.11635220125786164, 500, 1500, "jp@gc - WebDriver Sampler"], "isController": false}]}, function(index, item){
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
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 159, 25, 15.723270440251572, 4594.685534591195, 1107, 27421, 2354.0, 12141.0, 20471.0, 27185.800000000003, 1.912413851168497, 159.37780491123513, 0.0], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["jp@gc - WebDriver Sampler", 159, 25, 15.723270440251572, 4594.685534591195, 1107, 27421, 2354.0, 12141.0, 20471.0, 27185.800000000003, 1.912413851168497, 159.37780491123513, 0.0], "isController": false}]}, function(index, item){
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
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["The operation lasted too long: It took 18,654 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 16,256 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 12,141 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 21,097 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 27,029 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 16,113 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 24,632 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 11,818 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 5,398 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 24,903 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 17,147 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 8,993 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 20,471 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 9,229 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 9,412 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 8,137 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 10,224 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 9,779 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 14,202 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 21,925 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 14,745 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 6,000 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 17,818 milliseconds, but should not have lasted longer than 5,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 27,421 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}, {"data": ["The operation lasted too long: It took 23,030 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1, 4.0, 0.6289308176100629], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 159, 25, "The operation lasted too long: It took 18,654 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, "The operation lasted too long: It took 16,256 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, "The operation lasted too long: It took 12,141 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, "The operation lasted too long: It took 21,097 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, "The operation lasted too long: It took 27,029 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": ["jp@gc - WebDriver Sampler", 159, 25, "The operation lasted too long: It took 18,654 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, "The operation lasted too long: It took 16,256 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, "The operation lasted too long: It took 12,141 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, "The operation lasted too long: It took 21,097 milliseconds, but should not have lasted longer than 6,000 milliseconds.", 1, "The operation lasted too long: It took 27,029 milliseconds, but should not have lasted longer than 10,000 milliseconds.", 1], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
