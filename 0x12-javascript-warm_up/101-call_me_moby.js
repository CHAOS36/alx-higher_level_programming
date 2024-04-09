#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let pipo = 0; pipo < x; pipo++) {
    theFunction();
  }
};
