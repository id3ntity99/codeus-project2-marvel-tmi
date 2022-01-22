import { AnimatePresence } from "framer-motion";
import React, { useState } from "react";
import { IavengersInfo } from "../../typings/db";
import {
  PostZone,
  Post,
  Name,
  Description,
  Info,
  PopUpWrapper,
  PopUp,
  Title,
  PopupHeader,
  CancelBtn,
  PopUpInfo,
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
    console.log(avengerInfo);
    setToggleClicked(prev => !prev);
  };
  const onStopPropagation = (e: React.MouseEvent<HTMLDivElement>) => {
    e.stopPropagation();
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
            <Description>
              {avengerInfo.description
                ? avengerInfo.description
                : "Description 준비중.."}
            </Description>
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
            <PopUp onClick={onStopPropagation} layoutId={`${avengerInfo.id}`}>
              <PopupHeader>
                <Title>{avengerInfo.name}</Title>
                <CancelBtn onClick={onShowPopup}>
                  <svg width="20" height="20" viewBox="0 0 24 24">
                    <path
                      d="M2.29297 3.70706L10.5859 12L2.29297 20.2928L3.70718 21.7071L12.0001 13.4142L20.293 21.7071L21.7072 20.2928L13.4143 12L21.7072 3.70706L20.293 2.29285L12.0001 10.5857L3.70718 2.29285L2.29297 3.70706Z"
                      fill="currentColor"
                    ></path>
                  </svg>
                </CancelBtn>
              </PopupHeader>
              <PopUpInfo>
                <div>
                  <h5>Description</h5>
                  <p>{avengerInfo.description}</p>
                </div>
                <div>
                  <h5>Appearances</h5>
                  <p>{avengerInfo.appearances}</p>
                </div>
                <div>
                  <h5>Gender</h5>
                  <p>{avengerInfo.gender}</p>
                </div>
                <div>
                  <h5>Year</h5>
                  <p>{avengerInfo.year}</p>
                </div>
                <div>
                  <h5>Year since joining</h5>
                  <p>{avengerInfo.years_since_joining}</p>
                </div>
                <div>
                  <h5>URL</h5>
                  <p>
                    <a href={`${avengerInfo.url}`}>{avengerInfo.url}</a>
                  </p>
                </div>
              </PopUpInfo>
            </PopUp>
          </PopUpWrapper>
        )}
      </AnimatePresence>
    </>
  );
};

export default Avenger;
