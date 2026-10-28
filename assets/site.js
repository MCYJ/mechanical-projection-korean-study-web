'use strict';
const note=document.getElementById('coordinate-note');
if(note){
 const inputs=['x','y','z'].map(a=>document.getElementById('axis-'+a));
 const draw=(id,a,b,label)=>{const grid=document.getElementById(id);grid.replaceChildren();grid.setAttribute('aria-label',label);for(let row=2;row>=0;row--)for(let col=0;col<3;col++){const cell=document.createElement('span');cell.setAttribute('aria-hidden','true');if(col===a&&row===b)cell.className='on';grid.append(cell);}};
 const update=()=>{const [x,y,z]=inputs.map(i=>Number(i.value));['x','y','z'].forEach((a,i)=>document.getElementById('label-'+a).value=String([x,y,z][i]));draw('front',x,z,'X'+x+' Z'+z);draw('top',x,y,'X'+x+' Y'+y);draw('right',y,z,'Y'+y+' Z'+z);document.getElementById('coordinate-summary').value=`(${x},${y},${z}) → XZ(${x},${z}) / XY(${x},${y}) / YZ(${y},${z})`;};
 inputs.forEach(i=>i.addEventListener('input',update));update();
}
