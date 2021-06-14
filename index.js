const dpapi = require("bindings")("win-dpapi");

module.exports.protectData = dpapi.protectData;
module.exports.unprotectData = dpapi.unprotectData;
