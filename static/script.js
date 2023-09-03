//   service  

const formBudgetItems = document.querySelectorAll('.form__budget-item[data-aos="random"]');

  formBudgetItems.forEach(item => {
      const randomAOS = Math.random() < 0.5 ? 'fade-right' : 'fade-left';
      item.setAttribute('data-aos', randomAOS);
  });

  


  const progressSteps = document.querySelectorAll('.step-number');
  const formDetailSections = document.querySelectorAll('.form__budget-item');

  progressSteps.forEach((step, index) => {
      step.addEventListener('click', () => {
          formDetailSections[index].scrollIntoView({ behavior: 'smooth' });
      });
  });

  window.addEventListener('scroll', () => {
      formDetailSections.forEach((section, index) => {
          const rect = section.getBoundingClientRect();
          if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
              progressSteps.forEach(step => step.classList.remove('activ'));
              progressSteps[index].classList.add('activ');
          }
      });
  });