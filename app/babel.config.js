// module.exports = {
//   presets: [
//     '@vue/app'
//   ]
// }
module.exports = {
  presets: [
    [
      "@babel/preset-env",
      {
        useBuiltIns: "usage",
        corejs: 3,
      },
    ],
  ],
};