(function () {
  var katexOptions = [
    "displayMode",
    "leqno",
    "fleqn",
    "throwOnError",
    "errorColor",
    "strict",
    "output",
    "trust",
    "macros",
  ];

  var katexOptions2 = {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false },
      { left: "\\(", right: "\\)", display: false },
      { left: "\\begin{equation}", right: "\\end{equation}", display: true },
      { left: "\\begin{equation*}", right: "\\end{equation*}", display: true },
      { left: "\\begin{align}", right: "\\end{align}", display: true },
      { left: "\\begin{alignat}", right: "\\end{alignat}", display: true },
      { left: "\\begin{gather}", right: "\\end{gather}", display: true },
      { left: "\\begin{CD}", right: "\\end{CD}", display: true },
      { left: "\\[", right: "\\]", display: true },
    ],
    // • rendering keys, e.g.:
    throwOnError: false,
  };

  let titles = document.querySelectorAll(".title");
  let titlePre = document.getElementById("id_title");
  let titlePost = document.getElementById("exercise_title");
  let exercisePre = document.getElementById("id_text");
  let exercisePost = document.getElementById("demo-output");
  let solutionPre = document.getElementById("id_solution");
  let solutionPost = document.getElementById("demo-output2");

  toRenderSingle = [...titles];
  if (exercisePost) {
    toRenderSingle.push(exercisePost);
  }
  if (solutionPost) {
    toRenderSingle.push(solutionPost);
  }

  toRenderDouble = [
    [titlePre, titlePost],
    [exercisePre, exercisePost],
    [solutionPre, solutionPost],
  ];

  function renderElement(el) {
    try {
      renderMathInElement(el, katexOptions2);
    } catch (err) {
      while (el.lastChild) {
        el.removeChild(el.lastChild);
      }
      var msg = document.createTextNode(err.message);
      var span = document.createElement("span");
      span.appendChild(msg);
      el.appendChild(span);
      span.setAttribute("class", "errorMessage");
    }
  }

  toRenderDouble.forEach(([pre, post]) => {
    if (pre) {
      post.innerHTML = pre.value;
      renderElement(post);

      pre.addEventListener("input", () => {
        post.innerHTML = pre.value;
        renderElement(post);
      });
    }
  });

  toRenderSingle.forEach((el) => {
    renderElement(el);
  });
})();
