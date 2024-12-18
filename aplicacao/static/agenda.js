const calendar = document.querySelector(".calendar"),
 date = document.querySelector(".date"),
 daysContainer = document.querySelector(".days"),
 prev = document.querySelector(".prev"),
 next = document.querySelector(".next"),
 todayBtn = document.querySelector(".today-btn"),
 gotoBtn = document.querySelector(".goto-btn"),
 dateInput = document.querySelector(".date-input"),
 eventDay = document.querySelector(".event-day"),
 weekdays = document.querySelector("weekdays"),
 eventDate = document.querySelector(".event-date"),
 eventsContainer = document.querySelector(".events"),
 addEventBtn = document.querySelector(".add-event"),
 addEventWrapper = document.querySelector(".add-event-wrapper "),
 addEventCloseBtn = document.querySelector(".close "),
 addEventTitle = document.querySelector(".event-name "),
 addEventFrom = document.querySelector(".event-time-from "),
 addEventTo = document.querySelector(".event-time-to "),
 addEventSubmit = document.querySelector(".add-event-btn ");


let today = new Date();
let activeDay;
let month = today.getMonth();
let year = today.getFullYear();


const months = [
 "Janeiro",
 "Fevereiro",
 "Março",
 "Abril",
 "Maio",
 "Junho",
 "Julho",
 "Agosto",
 "Setembro",
 "Outubro",
 "Novembro",
 "Dezembro",
];


const eventsArr = [
 "Dom",
 "Seg",
 "Ter",
 "Qua",
 "Qui",
 "Sex",
 "Sab",
];
getEvents();
console.log(eventsArr);


//função para adicionar dias em dias com dia de aula e data anterior próxima data no mês anterior e dias do próximo mês e ativo hoje
// Array de feriados nacionais no Brasil
const feriados = [
   { day: 1, month: 1, title: "Ano Novo" },
   { day: 21, month: 4, title: "Tiradentes" },
   { day: 1, month: 5, title: "Dia do Trabalhador" },
   { day: 7, month: 9, title: "Independência do Brasil" },
   { day: 12, month: 10, title: "Nossa Senhora Aparecida" },
   { day: 2, month: 11, title: "Finados" },
   { day: 15, month: 11, title: "Proclamação da República" },
   { day: 25, month: 12, title: "Natal" },
   { day: 12, month: 2, title: "Carnaval" },
   { day: 13, month: 2, title: "Carnaval" },
   { day: 14, month: 2, title: "Carnaval" },
   { day: 18, month: 4, title: "Sexta-feira Santa"},
   { day: 28, month: 10, title: "Nossa Senhora da Penha"},
 ];
  // Função para inicializar o calendário
 function initCalendar() {
   const firstDay = new Date(year, month, 1);
   const lastDay = new Date(year, month + 1, 0);
   const prevLastDay = new Date(year, month, 0);
   const prevDays = prevLastDay.getDate();
   const lastDate = lastDay.getDate();
   const day = firstDay.getDay();
   const nextDays = 7 - lastDay.getDay() - 1;
    date.innerHTML = months[month] + " " + year;
    let days = "";
    // Dias do mês anterior
   for (let x = day; x > 0; x--) {
     days += `<div class="day prev-date">${prevDays - x + 1}</div>`;
   }
    // Dias do mês atual
   for (let i = 1; i <= lastDate; i++) {
     let event = false;
     let isHoliday = false;
      // Verifica se é um evento
     eventsArr.forEach((eventObj) => {
       if (eventObj.day === i && eventObj.month === month + 1 && eventObj.year === year) {
         event = true;
       }
     });
      // Verifica se é um feriado
     feriados.forEach((holiday) => {
       if (holiday.day === i && holiday.month === month + 1) {
         isHoliday = true;
       }
     });
      if (i === new Date().getDate() && year === new Date().getFullYear() && month === new Date().getMonth()) {
       activeDay = i;
       getActiveDay(i);
       updateEvents(i);
       if (event) {
         days += `<div class="day today active event">${i}</div>`;
       } else if (isHoliday) {
         days += `<div class="day today active holiday">${i}</div>`;
       } else {
         days += `<div class="day today active">${i}</div>`;
       }
     } else {
       if (event) {
         days += `<div class="day event">${i}</div>`;
       } else if (isHoliday) {
         days += `<div class="day holiday">${i}</div>`;
       } else {
         days += `<div class="day">${i}</div>`;
       }
     }
   }
    // Dias do próximo mês
   for (let j = 1; j <= nextDays; j++) {
     days += `<div class="day next-date">${j}</div>`;
   }
    daysContainer.innerHTML = days;
   addListner();
 }
  // Adicione um estilo para os feriados no CSS
 // .holiday { color: red; font-weight: bold; }
 //função para adicionar mês e ano no botão anterior e próximo
function prevMonth() {
 month--;
 if (month < 0) {
   month = 11;
   year--;
 }
 initCalendar();
}


function nextMonth() {
 month++;
 if (month > 11) {
   month = 0;
   year++;
 }
 initCalendar();
}


prev.addEventListener("click", prevMonth);
next.addEventListener("click", nextMonth);


initCalendar();


//função para adicionar ativo no dia
function addListner() {
 const days = document.querySelectorAll(".day");
 days.forEach((day) => {
   day.addEventListener("click", (e) => {
     getActiveDay(e.target.innerHTML);
     updateEvents(Number(e.target.innerHTML));
     activeDay = Number(e.target.innerHTML);
     //remove active
     days.forEach((day) => {
       day.classList.remove("active");
     });
     //se clicar na data anterior ou na próxima muda para esse mês
     if (e.target.classList.contains("prev-date")) {
       prevMonth();
       //add active to clicked day afte month is change
       setTimeout(() => {
         //add active where no prev-date or next-date
         const days = document.querySelectorAll(".day");
         days.forEach((day) => {
           if (
             !day.classList.contains("prev-date") &&
             day.innerHTML === e.target.innerHTML
           ) {
             day.classList.add("active");
           }
         });
       }, 100);
     } else if (e.target.classList.contains("next-date")) {
       nextMonth();
       //add active to clicked day afte month is changed
       setTimeout(() => {
         const days = document.querySelectorAll(".day");
         days.forEach((day) => {
           if (
             !day.classList.contains("next-date") &&
             day.innerHTML === e.target.innerHTML
           ) {
             day.classList.add("active");
           }
         });
       }, 100);
     } else {
       e.target.classList.add("active");
     }
   });
 });
}


todayBtn.addEventListener("click", () => {
 today = new Date();
 month = today.getMonth();
 year = today.getFullYear();
 initCalendar();
});


dateInput.addEventListener("input", (e) => {
 dateInput.value = dateInput.value.replace(/[^0-9/]/g, "");
 if (dateInput.value.length === 2) {
   dateInput.value += "/";
 }
 if (dateInput.value.length > 7) {
   dateInput.value = dateInput.value.slice(0, 7);
 }
 if (e.inputType === "deleteContentBackward") {
   if (dateInput.value.length === 3) {
     dateInput.value = dateInput.value.slice(0, 2);
   }
 }
});


gotoBtn.addEventListener("click", gotoDate);


function gotoDate() {
 console.log("here");
 const dateArr = dateInput.value.split("/");
 if (dateArr.length === 2) {
   if (dateArr[0] > 0 && dateArr[0] < 13 && dateArr[1].length === 4) {
     month = dateArr[0] - 1;
     year = dateArr[1];
     initCalendar();
     return;
   }
 }
 alert("Essa data não existe!");
}


//função obtém nome e data do dia ativo e atualiza eventday eventdate
function getActiveDay(date) {
   const day = new Date(year, month, date);
   const dayNameEnglish = day.toString().split(" ")[0];
    // Traduzindo o nome dos dias da semana para português
   const daysOfWeek = {
     Sun: "Dom",
     Mon: "Seg",
     Tue: "Ter",
     Wed: "Qua",
     Thu: "Qui",
     Fri: "Sex",
     Sat: "Sab",
   };
    const dayNamePortuguese = daysOfWeek[dayNameEnglish] || dayNameEnglish;
    eventDay.innerHTML = dayNamePortuguese;
   eventDate.innerHTML = date + " " + months[month] + " " + year;
 }


//function update events when a day is active
// Array de feriados nacionais no Brasil




// Função para verificar se o dia ativo é um feriado
function getHoliday(day, month) {
 return feriados.find((holiday) => holiday.day === day && holiday.month === month + 1);
}


// Função para atualizar os eventos, incluindo feriados
// Função para atualizar os eventos, incluindo feriados
function updateEvents(date) {
   let events = "";
    // Verifica se o dia ativo é um feriado
   const holiday = getHoliday(date, month);
   if (holiday) {
     events += `<div class="event holiday-event">
             <div class="title">
               <i class="fas fa-circle"></i>
               <h3 class="event-title">${holiday.title}</h3>
             </div>
             <div class="event-time">
               <span class="event-time">Feriado</span>
             </div>
         </div>`;
   }
    // Adiciona os eventos programados
   eventsArr.forEach((event) => {
     if (date === event.day && month + 1 === event.month && year === event.year) {
       event.events.forEach((event) => {
         events += `<div class="event">
             <div class="title">
               <i class="fas fa-circle"></i>
               <h3 class="event-title">${event.title}</h3>
             </div>
             <div class="event-time">
               <span class="event-time">${event.time}</span>
             </div>
         </div>`;
       });
     }
   });
    if (events === "") {
     events = `<div class="no-event">
             <h3>Sem eventos</h3>
         </div>`;
   }
  
   eventsContainer.innerHTML = events;
   saveEvents();
 }


//function to add event
addEventBtn.addEventListener("click", () => {
 addEventWrapper.classList.toggle("active");
});


addEventCloseBtn.addEventListener("click", () => {
 addEventWrapper.classList.remove("active");
});


document.addEventListener("click", (e) => {
 if (e.target !== addEventBtn && !addEventWrapper.contains(e.target)) {
   addEventWrapper.classList.remove("active");
 }
});


//allow 50 chars in eventtitle
addEventTitle.addEventListener("input", (e) => {
 addEventTitle.value = addEventTitle.value.slice(0, 60);
});






//allow only time in eventtime from and to
addEventFrom.addEventListener("input", (e) => {
 addEventFrom.value = addEventFrom.value.replace(/[^0-9:]/g, "");
 if (addEventFrom.value.length === 2) {
   addEventFrom.value += ":";
 }
 if (addEventFrom.value.length > 5) {
   addEventFrom.value = addEventFrom.value.slice(0, 5);
 }
});


addEventTo.addEventListener("input", (e) => {
 addEventTo.value = addEventTo.value.replace(/[^0-9:]/g, "");
 if (addEventTo.value.length === 2) {
   addEventTo.value += ":";
 }
 if (addEventTo.value.length > 5) {
   addEventTo.value = addEventTo.value.slice(0, 5);
 }
});


//function to add event to eventsArr
addEventSubmit.addEventListener("click", () => {
 const eventTitle = addEventTitle.value;
 const eventTimeFrom = addEventFrom.value;
 const eventTimeTo = addEventTo.value;
 if (eventTitle === "" || eventTimeFrom === "" || eventTimeTo === "") {
   alert("Please fill all the fields");
   return;
 }


 //check correct time format 24 hour
 const timeFromArr = eventTimeFrom.split(":");
 const timeToArr = eventTimeTo.split(":");
 if (
   timeFromArr.length !== 2 ||
   timeToArr.length !== 2 ||
   timeFromArr[0] > 23 ||
   timeFromArr[1] > 59 ||
   timeToArr[0] > 23 ||
   timeToArr[1] > 59
 ) {
   alert("Formato de hora inválido");
   return;
 }


 const timeFrom = convertTime(eventTimeFrom);
 const timeTo = convertTime(eventTimeTo);


 //check if event is already added
 let eventExist = false;
 eventsArr.forEach((event) => {
   if (
     event.day === activeDay &&
     event.month === month + 1 &&
     event.year === year
   ) {
     event.events.forEach((event) => {
       if (event.title === eventTitle) {
         eventExist = true;
       }
     });
   }
 });
 if (eventExist) {
   alert("Event already added");
   return;
 }
 const newEvent = {
   title: eventTitle,
   time: timeFrom + " - " + timeTo,
 };
 console.log(newEvent);
 console.log(activeDay);
 let eventAdded = false;
 if (eventsArr.length > 0) {
   eventsArr.forEach((item) => {
     if (
       item.day === activeDay &&
       item.month === month + 1 &&
       item.year === year
     ) {
       item.events.push(newEvent);
       eventAdded = true;
     }
   });
 }


 if (!eventAdded) {
   eventsArr.push({
     day: activeDay,
     month: month + 1,
     year: year,
     events: [newEvent],
   });
 }


 console.log(eventsArr);
 addEventWrapper.classList.remove("active");
 addEventTitle.value = "";
 addEventFrom.value = "";
 addEventTo.value = "";
 updateEvents(activeDay);
 //select active day and add event class if not added
 const activeDayEl = document.querySelector(".day.active");
 if (!activeDayEl.classList.contains("event")) {
   activeDayEl.classList.add("event");
 }
});


//function to delete event when clicked on event
eventsContainer.addEventListener("click", (e) => {
 if (e.target.classList.contains("event")) {
   if (confirm("Tem certeza de que deseja excluir este evento?")) {
     const eventTitle = e.target.children[0].children[1].innerHTML;
     eventsArr.forEach((event) => {
       if (
         event.day === activeDay &&
         event.month === month + 1 &&
         event.year === year
       ) {
         event.events.forEach((item, index) => {
           if (item.title === eventTitle) {
             event.events.splice(index, 1);
           }
         });
         //if no events left in a day then remove that day from eventsArr
         if (event.events.length === 0) {
           eventsArr.splice(eventsArr.indexOf(event), 1);
           //remove event class from day
           const activeDayEl = document.querySelector(".day.active");
           if (activeDayEl.classList.contains("event")) {
             activeDayEl.classList.remove("event");
           }
         }
       }
     });
     updateEvents(activeDay);
   }
 }
});


//function to save events in local storage
function saveEvents() {
 localStorage.setItem("events", JSON.stringify(eventsArr));
}


//function to get events from local storage
function getEvents() {
 //check if events are already saved in local storage then return event else nothing
 if (localStorage.getItem("events") === null) {
   return;
 }
 eventsArr.push(...JSON.parse(localStorage.getItem("events")));
}


function convertTime(time) {
   //convert time to 24 hour format
   let timeArr = time.split(":");
   let timeHour = timeArr[0];
   let timeMin = timeArr[1];
   let timeFormat = timeHour >= 12 ? "PM" : "AM";
   timeHour = timeHour % 12 || 12;
   time = timeHour + ":" + timeMin + " " + timeFormat;
   return time;
 }