// import original module declarations
import "styled-components";

// and extend them!
declare module "styled-components" {
  export interface DefaultTheme {
    textColor: string;
    bgColor: { default: string; lighter: string };
    accentColor: string;
  }
  export interface LighteTheme {
    textColor: string;
    bgColor: { default: string; lighter: string };
    accentColor: string;
  }
}
