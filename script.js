'use strict';

// Keep animation opt-in: a static first frame also works without JavaScript.
const gif = document.querySelector('#space-gif');
const motionToggle = document.querySelector('#motion-toggle');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const still = 'assets/astronaut-still.png';
const animation = 'https://media.tenor.com/vcJT8QZ8EgEAAAAM/izzeh-lost.gif';

if (gif && motionToggle) {
  let playing = false;
  function setMotion(enabled) {
    playing = enabled;
    gif.src = enabled ? animation : still;
    motionToggle.textContent = enabled ? 'Stop GIF' : 'Play GIF';
  }
  motionToggle.hidden = false;
  motionToggle.removeAttribute('aria-pressed');
  gif.referrerPolicy = 'no-referrer';
  motionToggle.addEventListener('click', () => setMotion(!playing));
  function handleMotionPreference(event) {
    if (event.matches) setMotion(false);
  }
  if (reducedMotion.addEventListener) {
    reducedMotion.addEventListener('change', handleMotionPreference);
  } else if (reducedMotion.addListener) {
    reducedMotion.addListener(handleMotionPreference);
  }
  document.addEventListener('visibilitychange', () => {
    if (document.hidden && playing) setMotion(false);
  });
  gif.addEventListener('error', () => {
    if (playing) {
      setMotion(false);
      motionToggle.textContent = 'Retry GIF';
    }
  });
}
