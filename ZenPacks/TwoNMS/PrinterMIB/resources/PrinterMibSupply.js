(function(){

var ZC = Ext.ns('Zenoss.component');


function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}



ZC.PrinterSupplyPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PrinterSupply',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'Description'},
                {name: 'CurrentLevel'},
                {name: 'CurrentUsage'},
                {name: 'MaxLevel'},
                {name: 'usesMonitorAttribute'},
                {name: 'SupplyType'},
                {name: 'SupplyTypeUnit'},
                {name: 'hasMonitor'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },
/*             {
                id: 'name',
                dataIndex: 'name',
                header: _t('ID'),
                sortable: true,
            },
*/            {
                id: 'Description',
                dataIndex: 'Description',
                header: _t('Description'),
                sortable: true,
                width: 300
            },{
                id: 'SupplyType',
                dataIndex: 'SupplyType',
                header: _t('Type'),
                sortable: true
            },{
                id: 'CurrentUsage',
                dataIndex: 'CurrentUsage',
                header: _t('Usage pct'),
                sortable: true
            },{
                id: 'CurrentLevel',
                dataIndex: 'CurrentLevel',
                header: _t('Current Level'),
                sortable: true
            },{
                id: 'MaxLevel',
                dataIndex: 'MaxLevel',
                header: _t('Max Level'),
                sortable: true
            },{
                id: 'SupplyTypeUnit',
                dataIndex: 'SupplyTypeUnit',
                header: _t('Unit'),
                sortable: true
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                width: 60
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons
            }]

        });
        ZC.PrinterSupplyPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PrinterSupplyPanel', ZC.PrinterSupplyPanel);
ZC.registerName('PrinterSupply', _t('PrinterSupply'), _t('Printer Supplies'));
})();
