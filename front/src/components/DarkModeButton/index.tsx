import { useState } from "react";
import { Circle, ModeZone, ToggleButton, Light, Dark } from "./styles";

const DarkModeButton = () => {
  const [show, setShow] = useState(false);
  const onShowCircle = () => {
    setShow(prev => !prev);
  };
  return (
    <ToggleButton>
      <ModeZone>
        {show ? <Circle layoutId="mode" onClick={onShowCircle} /> : null}
        <Light width="18" height="18" viewBox="0 0 28 28" fill="#FEDF4E">
          <path d="M3.55,18.54L4.96,19.95L6.76,18.16L5.34,16.74M11,22.45C11.32,22.45 13,22.45 13,22.45V19.5H11M12,5.5A6,6 0 0,0 6,11.5A6,6 0 0,0 12,17.5A6,6 0 0,0 18,11.5C18,8.18 15.31,5.5 12,5.5M20,12.5H23V10.5H20M17.24,18.16L19.04,19.95L20.45,18.54L18.66,16.74M20.45,4.46L19.04,3.05L17.24,4.84L18.66,6.26M13,0.55H11V3.5H13M4,10.5H1V12.5H4M6.76,4.84L4.96,3.05L3.55,4.46L5.34,6.26L6.76,4.84Z"></path>
        </Light>
      </ModeZone>
      <ModeZone>
        {!show ? <Circle layoutId="mode" onClick={onShowCircle} /> : null}
        <Dark width="18" height="18" viewBox="0 0 28 28" fill="#FEDF4E">
          <path
            fill-rule="evenodd"
            d="M10,2C8.18,2 6.47,2.5 5,3.35C8,5.08 10,8.3 10,12C10,15.7 8,18.92 5,20.65C6.47,21.5 8.18,22 10,22A10,10 0 0,0 20,12A10,10 0 0,0 10,2Z"
          ></path>
        </Dark>
      </ModeZone>
    </ToggleButton>
  );
};

export default DarkModeButton;
