#!/usr/bin/node

exports.esrever = function (list) {
  const NewList = [];
  for (let i = 0; i < list.length; i++) {
    NewList.push(list[list.length - i - 1]);
  }
  return (NewList);
};
