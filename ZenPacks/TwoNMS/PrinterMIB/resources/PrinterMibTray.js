(function(){

var ZC = Ext.ns('Zenoss.component');


function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}


ZC.PrinterTrayPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PrinterTray',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'InputName'},
                {name: 'Model'},
                {name: 'Type'},
                {name: 'CurrentUsage'},
                {name: 'CurrentLevel'},
                {name: 'MaxLevel'},
                {name: 'Unit'},
                {name: 'Description'},
                {name: 'MediaName'},
                {name: 'usesMonitorAttribute'},
                {name: 'hasMonitor'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'InputName',
                dataIndex: 'InputName',
                header: _t('Name'),
                sortable: true,
            },{
                id: 'Model',
                dataIndex: 'Model',
                header: _t('Model'),
                sortable: true,
                width: 150
            },{
                id: 'Type',
                dataIndex: 'Type',
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
                id: 'Unit',
                dataIndex: 'Unit',
                header: _t('Unit'),
                sortable: true
            },{
                id: 'Description',
                dataIndex: 'Description',
                header: _t('Description'),
                sortable: true
            },{
                id: 'MediaName',
                dataIndex: 'MediaName',
                header: _t('Media Name'),
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
        ZC.PrinterTrayPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PrinterTrayPanel', ZC.PrinterTrayPanel);
ZC.registerName('PrinterTray', _t('PrinterTray'), _t('Printer Input Trays'));
})();
