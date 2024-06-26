/*---모달 공통-----*/
var modal = document.getElementById("modal-box");
var modal_btn = document.getElementById("modal-open");
var modal_span = document.getElementsByClassName("modal-close")[0];
var form = document.querySelector('#modal-box form');
var imgElement = form.querySelector('.embed-img');
var containerImg = document.getElementsByClassName("container-img")[0];

modal_btn.onclick = function() {
  if (containerImg){
    containerImg.style.display = 'none';
  }
  modal.style.display = "block";
}
modal_span.onclick = function() {
  modal.style.display = "none";
  // 초기화
  form.removeAttribute('action');
  if(form.querySelector('input[name="title"]')){
    form.querySelector('input[name="title"]').value = '';
  }
  if(form.querySelector('input[name="name"]')){
    form.querySelector('input[name="name"]').value = '';
  }
  if(form.querySelector('textarea[name="contents"]')){
    form.querySelector('textarea[name="contents"]').value = '';
  }
  if(imgElement){
    imgElement.removeAttribute('alt');
    imgElement.removeAttribute('src');
  }
}

/**수정 버튼 */
var editButtons = document.querySelectorAll('.lecture-edit');
// 각 버튼에 이벤트 리스너를 추가
editButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    /**해당 요소 ID 값 */
    var id = this.dataset.id;
    /**선택된 요소 */
    var lectureElement;
    
    // 전체 강의
    if (document.querySelector('a[href="/lecture/list/detail/' + id + '"]')){
      lectureElement = document.querySelector('a[href="/lecture/list/detail/' + id + '"]');
      lectureElement.foundBy = 'aTag';
    }
    // 세부 강의
    else if(document.querySelector('div[data-lecture-id="' + id + '"]')){
      lectureElement = document.querySelector('div[data-lecture-id="' + id + '"]')
      lectureElement.foundBy = 'lecture';
      console.log(lectureElement)
    }
    // 메인 슬라이더
    else if (document.querySelector('div[data-slide-id="' + id + '"]')){
      lectureElement = document.querySelector('div[data-slide-id="' + id + '"]');
      lectureElement.foundBy = 'slide';
    }
    else{
      console.log("Edit Button Error!")
    }
    
    var title = lectureElement.querySelector('.lecture-title').textContent;
    var contents = lectureElement.querySelector('.lecture-text').innerHTML;
    var contentText = contents.replace(/<br>/g, '\n');
    var image = lectureElement.querySelector('img').dataset.src;
  
  if (lectureElement) {
    if (lectureElement.foundBy === 'aTag') {
      form.action = "list/update/" + id;
    }
    else if (lectureElement.foundBy === 'lecture') {
      form.action = "/lecture/list/detail/update/" + id;
    }
    else if (lectureElement.foundBy === 'slide') {
      form.action = "slide/update/" + id;
    }
  }
    
    form.querySelector('input[name="title"]').value = title;
    form.querySelector('textarea[name="contents"]').value = contentText
    
    // 이미지 src 설정
    imgElement.src = image;
    imgElement.alt = title;

    var inputCheck = form.querySelector('.hidden-checkbox');
    inputCheck.value = id;

    containerImg.removeAttribute('style');

    modal.style.display = "block";
  });
});

// 강사소개
var editButtons = document.querySelectorAll('.instrs-edit');
// 각 버튼에 이벤트 리스너를 추가
editButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    var id = this.dataset.id;
    // 부모 클래스를 가져옴
    var parent = this.parentNode;
    var name = parent.querySelector('.instrs-name').textContent;
    var contents = parent.querySelector('.instrs-text').innerHTML;
    var contentText = contents.replace(/<br>/g, '\n');
    var image = parent.querySelector('img').dataset.src;

    form.action = "update/" + id;
    form.querySelector('input[name="name"]').value = name;
    form.querySelector('textarea[name="contents"]').value = contentText
    
    // 이미지 src 설정
    imgElement.src = image;
    imgElement.alt = name;

    var inputCheck = form.querySelector('.hidden-checkbox');
    inputCheck.value = id;

    containerImg.removeAttribute('style');

    modal.style.display = "block";
  });
});