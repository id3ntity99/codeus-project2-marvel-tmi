import { AnimatePresence } from "framer-motion";
import { useState } from "react";
import { IavengersInfo } from "../../typings/db";
import {
  PostZone,
  Post,
  Name,
  Description,
  Info,
  PopUpWrapper,
  PopUp,
} from "./styles";

interface IAvengerProps {
  avengerInfo: IavengersInfo;
}

const postZoneVariants = {
  start: { translateY: 0 },
  hover: { translateY: -10 },
};

const Avenger = ({ avengerInfo }: IAvengerProps) => {
  const [toggleClicked, setToggleClicked] = useState(false);
  const onShowPopup = () => {
    setToggleClicked(prev => !prev);
  };
  return (
    <>
      <PostZone
        onClick={onShowPopup}
        variants={postZoneVariants}
        whileHover="hover"
      >
        <Post layoutId={`${avengerInfo.id}`}>
          <div style={{ padding: 10 }}>
            <Name>{avengerInfo.name}</Name>
            <Description>{avengerInfo.description}</Description>
          </div>
          <Info>
            <div>성별: {avengerInfo.gender}</div>
            <div>출연수: {avengerInfo.appearances}</div>
          </Info>
        </Post>
      </PostZone>
      <AnimatePresence>
        {toggleClicked && (
          <PopUpWrapper
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onShowPopup}
          >
            <PopUp layoutId={`${avengerInfo.id}`}></PopUp>
          </PopUpWrapper>
        )}
      </AnimatePresence>
    </>
  );
};

export default Avenger;
