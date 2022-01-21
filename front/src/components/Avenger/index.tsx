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
import { motion } from "framer-motion";

interface IAvengerProps {
  avengerInfo: IavengersInfo;
}

const Avenger = ({ avengerInfo }: IAvengerProps) => {
  const [toggleClicked, setToggleClicked] = useState(false);
  const onClick = () => {
    setToggleClicked(prev => !prev);
  };
  return (
    <>
      <PostZone onClick={onClick}>
        {!toggleClicked ? (
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
        ) : null}
        {toggleClicked ? (
          <PopUpWrapper>
            <PopUp layoutId={`${avengerInfo.id}`}></PopUp>
          </PopUpWrapper>
        ) : null}
      </PostZone>
    </>
  );
};

export default Avenger;
