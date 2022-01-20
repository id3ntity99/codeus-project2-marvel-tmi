import { useQuery } from "react-query";
import styled from "styled-components";
import { IavengersInfo } from "../../typings/db";
import { fetcherAvengers } from "../../utils/api";
import { Post, Name, Description, Info } from "./styles";

interface IAvengerProps {
  avengerInfo: IavengersInfo;
}

const Avenger = ({ avengerInfo }: IAvengerProps) => {
  const onClick = () => {
    console.log(avengerInfo);
  };
  return (
    <Post onClick={onClick}>
      <div style={{ padding: 10 }}>
        <Name>{avengerInfo.name}</Name>
        <Description>{avengerInfo.description}</Description>
      </div>
      <Info>
        <div>성별: {avengerInfo.gender}</div>
        <div>출연수: {avengerInfo.appearances}</div>
      </Info>
    </Post>
  );
};

export default Avenger;
