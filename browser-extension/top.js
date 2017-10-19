"use strict";
{
  const oldinjection = `
    const ODEFP = Object.defineProperty;
    Object.defineProperty( Object, 'defineProperty', { get: () => defP } );
    function defP(...args) {
      console.log("Call to ODEFP", ...args );
      return ODEFP.call( Object, ...args );
    }
    const ODEFPs = Object.defineProperties;
    Object.defineProperty( Object, 'defineProperties', { get: () => defPs } );
    function defPs(...args) {
      console.log("Call to ODEFPs", ...args );
      return ODEFPs.call( Object, ...args );
    }
  `;
  const injection = `
      Object.defineProperty( window, 'self', { get : () => {throw new TypeError("FUCK YOU")} } );
  `;
  const script = document.createElement('script');
  script.type="text/javascript";
  script.textContent = injection;
  document.documentElement.appendChild(script);
  alert("Injected");
}
