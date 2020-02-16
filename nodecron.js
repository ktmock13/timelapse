var cron = require('node-cron');
var shell = require('shelljs');

cron.schedule('0 21 * * *', () => {
   shell.exec('./run.sh')
});