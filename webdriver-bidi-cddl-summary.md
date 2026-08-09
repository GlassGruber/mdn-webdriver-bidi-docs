# WebDriver BiDi - Extracted CDDL & Protocol Schemas

> File generato automaticamente dal sorgente ufficiale W3C per contesto LLM.


## Core Protocol Definitions

```cddl
Command = {
  id: js-uint,
  CommandData,
  Extensible,
}

CommandData = (
  BrowserCommand //
  BrowsingContextCommand //
  EmulationCommand //
  InputCommand //
  NetworkCommand //
  ScriptCommand //
  SessionCommand //
  StorageCommand //
  WebExtensionCommand
)

EmptyParams = {
   Extensible
}
```

```cddl
Message = (
  CommandResponse /
  ErrorResponse /
  Event
)

CommandResponse = {
  type: "success",
  id: js-uint,
  result: ResultData,
  Extensible
}

ErrorResponse = {
  type: "error",
  id: js-uint / null,
  error: ErrorCode,
  message: text,
  ? stacktrace: text,
  Extensible
}

ResultData = (
  BrowserResult /
  BrowsingContextResult /
  EmulationResult /
  InputResult /
  NetworkResult /
  ScriptResult /
  SessionResult /
  StorageResult /
  WebExtensionResult
)

EmptyResult = {
  Extensible
}

Event = {
  type: "event",
  EventData,
  Extensible
}

EventData = (
  BrowsingContextEvent //
  InputEvent //
  LogEvent //
  NetworkEvent //
  ScriptEvent
)
```

```cddl
Extensible = (*text => any)

js-int = -9007199254740991..9007199254740991
js-uint = 0..9007199254740991
```

```cddl
ErrorCode = "invalid argument" /
            "invalid selector" /
            "invalid session id" /
            "invalid web extension" /
            "move target out of bounds" /
            "no such alert" /
            "no such network collector" /
            "no such element" /
            "no such frame" /
            "no such handle" /
            "no such history entry" /
            "no such intercept" /
            "no such network data" /
            "no such node" /
            "no such request" /
            "no such screencast" /
            "no such script" /
            "no such storage partition" /
            "no such user context" /
            "no such web extension" /
            "session not created" /
            "unable to capture screen" /
            "unable to close browser" /
            "unable to set cookie" /
            "unable to set file input" /
            "unavailable network data" /
            "underspecified storage partition" /
            "unknown command" /
            "unknown error" /
            "unsupported operation"
```

## Module: session

```cddl
SessionCommand = (
  session.End //
  session.New //
  session.Status //
  session.Subscribe //
  session.Unsubscribe
)
```

```cddl
SessionResult = (
  session.EndResult /
  session.NewResult /
  session.StatusResult /
  session.SubscribeResult /
  session.UnsubscribeResult
)
```

```cddl
session.CapabilitiesRequest = {
  ? alwaysMatch: session.CapabilityRequest,
  ? firstMatch: [*session.CapabilityRequest]
}
```

```cddl
session.CapabilityRequest = {
  ? acceptInsecureCerts: bool,
  ? browserName: text,
  ? browserVersion: text,
  ? platformName: text,
  ? proxy: session.ProxyConfiguration,
  ? unhandledPromptBehavior: session.UserPromptHandler,
  Extensible
}
```

```cddl
session.ProxyConfiguration = {
   session.AutodetectProxyConfiguration //
   session.DirectProxyConfiguration //
   session.ManualProxyConfiguration //
   session.PacProxyConfiguration //
   session.SystemProxyConfiguration
}

session.AutodetectProxyConfiguration = (
   proxyType: "autodetect",
   Extensible
)

session.DirectProxyConfiguration = (
   proxyType: "direct",
   Extensible
)

session.ManualProxyConfiguration = (
   proxyType: "manual",
   ? httpProxy: text,
   ? sslProxy: text,
   ? session.SocksProxyConfiguration,
   ? noProxy: [*text],
   Extensible
)

session.SocksProxyConfiguration = (
   socksProxy: text,
   socksVersion: 0..255,
)

session.PacProxyConfiguration = (
   proxyType: "pac",
   proxyAutoconfigUrl: text,
   Extensible
)

session.SystemProxyConfiguration = (
   proxyType: "system",
   Extensible
)
```

```cddl
session.UserPromptHandler = {
  ? alert: session.UserPromptHandlerType,
  ? beforeUnload: session.UserPromptHandlerType,
  ? confirm: session.UserPromptHandlerType,
  ? default: session.UserPromptHandlerType,
  ? file: session.UserPromptHandlerType,
  ? prompt: session.UserPromptHandlerType,
}
```

```cddl
session.UserPromptHandlerType = "accept" / "dismiss" / "ignore";
```

```cddl
session.Subscription = text
```

```cddl
session.SubscribeParameters = {
  events: [+text],
  ? contexts: [+browsingContext.BrowsingContext],
  ? userContexts: [+browser.UserContext],
}
```

```cddl
session.UnsubscribeByIDRequest = {
  subscriptions: [+session.Subscription],
}
```

```cddl
session.UnsubscribeByAttributesRequest = {
  events: [+text],
}
```

```cddl
session.Status = (
        method: "session.status",
        params: EmptyParams,
      )
```

```cddl
session.StatusResult = {
        ready: bool,
        message: text,
      }
```

```cddl
session.New = (
        method: "session.new",
        params: session.NewParameters
      )

      session.NewParameters = {
        capabilities: session.CapabilitiesRequest
      }
```

```cddl
session.NewResult = {
        sessionId: text,
        capabilities: {
          acceptInsecureCerts: bool,
          browserName: text,
          browserVersion: text,
          platformName: text,
          setWindowRect: bool,
          userAgent: text,
          ? proxy: session.ProxyConfiguration,
          ? unhandledPromptBehavior: session.UserPromptHandler,
          ? webSocketUrl: text,
          Extensible
        }
      }
```

```cddl
session.End = (
        method: "session.end",
        params: EmptyParams
      )
```

```cddl
session.EndResult = EmptyResult
```

```cddl
session.Subscribe = (
        method: "session.subscribe",
        params: session.SubscribeParameters
      )
```

```cddl
session.SubscribeResult = {
          subscription: session.Subscription,
        }
```

```cddl
session.Unsubscribe = (
       method: "session.unsubscribe",
       params: session.UnsubscribeParameters,
     )

     session.UnsubscribeParameters = session.UnsubscribeByAttributesRequest / session.UnsubscribeByIDRequest
```

```cddl
session.UnsubscribeResult = EmptyResult
```

## Module: browser

```cddl
BrowserCommand = (
  browser.Close //
  browser.CreateUserContext //
  browser.GetClientWindows //
  browser.GetUserContexts //
  browser.RemoveUserContext //
  browser.SetClientWindowState //
  browser.SetDownloadBehavior
)
```

```cddl
BrowserResult = (
  browser.CloseResult /
  browser.CreateUserContextResult /
  browser.GetClientWindowsResult /
  browser.GetUserContextsResult /
  browser.RemoveUserContextResult /
  browser.SetClientWindowStateResult /
  browser.SetDownloadBehaviorResult
)
```

```cddl
browser.ClientWindow = text;
```

```cddl
browser.ClientWindowInfo = {
  active: bool,
  clientWindow: browser.ClientWindow,
  height: js-uint,
  state: "fullscreen" / "maximized" / "minimized" / "normal",
  width: js-uint,
  x: js-int,
  y: js-int,
}
```

```cddl
browser.UserContext = text;
```

```cddl
browser.UserContextInfo = {
  userContext: browser.UserContext
}
```

```cddl
browser.Close = (
        method: "browser.close",
        params: EmptyParams,
      )
```

```cddl
browser.CloseResult = EmptyResult
```

```cddl
browser.CreateUserContext = (
        method: "browser.createUserContext",
        params: browser.CreateUserContextParameters,
      )

      browser.CreateUserContextParameters = {
        ? acceptInsecureCerts: bool,
        ? proxy: session.ProxyConfiguration,
        ? unhandledPromptBehavior: session.UserPromptHandler
      }
```

```cddl
browser.CreateUserContextResult = browser.UserContextInfo
```

```cddl
browser.GetClientWindows = (
        method: "browser.getClientWindows",
        params: EmptyParams,
      )
```

```cddl
browser.GetClientWindowsResult = {
        clientWindows: [ * browser.ClientWindowInfo]
      }
```

```cddl
browser.GetUserContexts = (
        method: "browser.getUserContexts",
        params: EmptyParams,
      )
```

```cddl
browser.GetUserContextsResult = {
        userContexts: [ + browser.UserContextInfo]
      }
```

```cddl
browser.RemoveUserContext = (
        method: "browser.removeUserContext",
        params: browser.RemoveUserContextParameters
      )

      browser.RemoveUserContextParameters = {
        userContext: browser.UserContext
      }
```

```cddl
browser.RemoveUserContextResult = EmptyResult
```

```cddl
browser.SetClientWindowState = (
        method: "browser.setClientWindowState",
        params: browser.SetClientWindowStateParameters
      )

      browser.SetClientWindowStateParameters = {
        clientWindow: browser.ClientWindow,
        (browser.ClientWindowNamedState // browser.ClientWindowRectState)
      }

      browser.ClientWindowNamedState = (
        state: "fullscreen" / "maximized" / "minimized"
      )

      browser.ClientWindowRectState = (
        state: "normal",
        ? width: js-uint,
        ? height: js-uint,
        ? x: js-int,
        ? y: js-int,
      )
```

```cddl
browser.SetClientWindowStateResult = browser.ClientWindowInfo
```

```cddl
browser.SetDownloadBehavior = (
        method: "browser.setDownloadBehavior",
        params: browser.SetDownloadBehaviorParameters
      )

      browser.SetDownloadBehaviorParameters = {
        downloadBehavior: browser.DownloadBehavior / null,
        ? userContexts: [+browser.UserContext]
      }

      browser.DownloadBehavior = {
        (
          browser.DownloadBehaviorAllowed //
          browser.DownloadBehaviorDenied
        )
      }

      browser.DownloadBehaviorAllowed = (
        type: "allowed",
        destinationFolder: text
      )

      browser.DownloadBehaviorDenied = (
        type: "denied"
      )
```

```cddl
browser.SetDownloadBehaviorResult = EmptyResult
```

## Module: browsingContext

```cddl
BrowsingContextCommand = (
  browsingContext.Activate //
  browsingContext.CaptureScreenshot //
  browsingContext.Close //
  browsingContext.Create //
  browsingContext.GetTree //
  browsingContext.HandleUserPrompt //
  browsingContext.LocateNodes //
  browsingContext.Navigate //
  browsingContext.Print //
  browsingContext.Reload //
  browsingContext.SetBypassCSP //
  browsingContext.SetViewport //
  browsingContext.StartScreencast //
  browsingContext.StopScreencast //
  browsingContext.TraverseHistory
)
```

```cddl
BrowsingContextResult = (
  browsingContext.ActivateResult /
  browsingContext.CaptureScreenshotResult /
  browsingContext.CloseResult /
  browsingContext.CreateResult /
  browsingContext.GetTreeResult /
  browsingContext.HandleUserPromptResult /
  browsingContext.LocateNodesResult /
  browsingContext.NavigateResult /
  browsingContext.PrintResult /
  browsingContext.ReloadResult /
  browsingContext.SetBypassCSPResult /
  browsingContext.SetViewportResult /
  browsingContext.StartScreencastResult /
  browsingContext.StopScreencastResult /
  browsingContext.TraverseHistoryResult
)

BrowsingContextEvent = (
  browsingContext.ContextCreated //
  browsingContext.ContextDestroyed //
  browsingContext.DomContentLoaded //
  browsingContext.DownloadEnd //
  browsingContext.DownloadWillBegin //
  browsingContext.FragmentNavigated //
  browsingContext.HistoryUpdated //
  browsingContext.Load //
  browsingContext.NavigationAborted //
  browsingContext.NavigationCommitted //
  browsingContext.NavigationFailed //
  browsingContext.NavigationStarted //
  browsingContext.UserPromptClosed //
  browsingContext.UserPromptOpened
)
```

```cddl
browsingContext.BrowsingContext = text;
```

```cddl
browsingContext.InfoList = [*browsingContext.Info]

browsingContext.Info = {
  children: browsingContext.InfoList / null,
  clientWindow: browser.ClientWindow,
  context: browsingContext.BrowsingContext,
  originalOpener: browsingContext.BrowsingContext / null,
  url: text,
  userContext: browser.UserContext,
  ? parent: browsingContext.BrowsingContext / null,
}
```

```cddl
browsingContext.Locator = (
   browsingContext.AccessibilityLocator /
   browsingContext.CssLocator /
   browsingContext.ContextLocator /
   browsingContext.InnerTextLocator /
   browsingContext.XPathLocator
)

browsingContext.AccessibilityLocator = {
   type: "accessibility",
   value: {
    ? name: text,
    ? role: text,
   }
}

browsingContext.CssLocator = {
   type: "css",
   value: text
}

browsingContext.ContextLocator = {
  type: "context",
  value: {
    context: browsingContext.BrowsingContext,
  }
}

browsingContext.InnerTextLocator = {
   type: "innerText",
   value: text,
   ? ignoreCase: bool
   ? matchType: "full" / "partial",
   ? maxDepth: js-uint,
}

browsingContext.XPathLocator = {
   type: "xpath",
   value: text
}
```

```cddl
browsingContext.Navigation = text;
```

```cddl
browsingContext.Download = text;
```

```cddl
browsingContext.BaseNavigationInfo = (
  context: browsingContext.BrowsingContext,
  navigation: browsingContext.Navigation / null,
  timestamp: js-uint,
  url: text,
  ? userContext: browser.UserContext,
)

browsingContext.NavigationInfo = {
  browsingContext.BaseNavigationInfo
}
```

```cddl
browsingContext.ReadinessState = "none" / "interactive" / "complete"
```

```cddl
browsingContext.UserPromptType = "alert" / "beforeunload" / "confirm" / "prompt";
```

```cddl
browsingContext.Activate = (
        method: "browsingContext.activate",
        params: browsingContext.ActivateParameters
      )

      browsingContext.ActivateParameters = {
        context: browsingContext.BrowsingContext
      }
```

```cddl
browsingContext.ActivateResult = EmptyResult
```

```cddl
browsingContext.CaptureScreenshot = (
        method: "browsingContext.captureScreenshot",
        params: browsingContext.CaptureScreenshotParameters
      )

      browsingContext.CaptureScreenshotParameters = {
        context: browsingContext.BrowsingContext,
        ? origin: ("viewport" / "document") .default "viewport",
        ? format: browsingContext.ImageFormat,
        ? clip: browsingContext.ClipRectangle,
      }

      browsingContext.ImageFormat = {
         type: text,
         ? quality: 0.0..1.0,
      }

      browsingContext.ClipRectangle = (
        browsingContext.BoxClipRectangle /
        browsingContext.ElementClipRectangle
      )

      browsingContext.ElementClipRectangle = {
        type: "element",
        element: script.SharedReference
      }

      browsingContext.BoxClipRectangle = {
         type: "box",
         x: float,
         y: float,
         width: float,
         height: float
      }
```

```cddl
browsingContext.CaptureScreenshotResult = {
          data: text
        }
```

```cddl
browsingContext.Close = (
        method: "browsingContext.close",
        params: browsingContext.CloseParameters
      )

      browsingContext.CloseParameters = {
        context: browsingContext.BrowsingContext,
        ? promptUnload: bool .default false
      }
```

```cddl
browsingContext.CloseResult = EmptyResult
```

```cddl
browsingContext.Create = (
        method: "browsingContext.create",
        params: browsingContext.CreateParameters
      )

      browsingContext.CreateType = "tab" / "window"

      browsingContext.CreateParameters = {
        type: browsingContext.CreateType,
        ? referenceContext: browsingContext.BrowsingContext,
        ? background: bool .default false,
        ? userContext: browser.UserContext
      }
```

```cddl
browsingContext.CreateResult = {
          context: browsingContext.BrowsingContext,
          ? userContext: browser.UserContext
        }
```

```cddl
browsingContext.GetTree = (
        method: "browsingContext.getTree",
        params: browsingContext.GetTreeParameters
      )

      browsingContext.GetTreeParameters = {
        ? maxDepth: js-uint,
        ? root: browsingContext.BrowsingContext,
      }
```

```cddl
browsingContext.GetTreeResult = {
          contexts: browsingContext.InfoList
        }
```

```cddl
browsingContext.HandleUserPrompt = (
        method: "browsingContext.handleUserPrompt",
        params: browsingContext.HandleUserPromptParameters
      )

      browsingContext.HandleUserPromptParameters = {
        context: browsingContext.BrowsingContext,
        ? accept: bool,
        ? userText: text,
      }
```

```cddl
browsingContext.HandleUserPromptResult = EmptyResult
```

```cddl
browsingContext.LocateNodes = (
        method: "browsingContext.locateNodes",
        params: browsingContext.LocateNodesParameters
      )

      browsingContext.LocateNodesParameters = {
         context: browsingContext.BrowsingContext,
         locator: browsingContext.Locator,
         ? maxNodeCount: (js-uint .ge 1),
         ? serializationOptions: script.SerializationOptions,
         ? startNodes: [ + script.SharedReference ]
      }
```

```cddl
browsingContext.LocateNodesResult = {
            nodes: [ * script.NodeRemoteValue ]
        }
```

```cddl
browsingContext.Navigate = (
        method: "browsingContext.navigate",
        params: browsingContext.NavigateParameters
      )

      browsingContext.NavigateParameters = {
        context: browsingContext.BrowsingContext,
        url: text,
        ? wait: browsingContext.ReadinessState,
      }
```

```cddl
browsingContext.NavigateResult = {
          navigation: browsingContext.Navigation / null,
          url: text,
        }
```

```cddl
browsingContext.Print = (
        method: "browsingContext.print",
        params: browsingContext.PrintParameters
      )

      browsingContext.PrintParameters = {
        context: browsingContext.BrowsingContext,
        ? background: bool .default false,
        ? margin: browsingContext.PrintMarginParameters,
        ? orientation: ("portrait" / "landscape") .default "portrait",
        ? page: browsingContext.PrintPageParameters,
        ? pageRanges: [*(js-uint / text)],
        ? scale: (0.1..2.0) .default 1.0,
        ? shrinkToFit: bool .default true,
      }

      browsingContext.PrintMarginParameters = {
        ? bottom: (float .ge 0.0) .default 1.0,
        ? left: (float .ge 0.0) .default 1.0,
        ? right: (float .ge 0.0) .default 1.0,
        ? top: (float .ge 0.0) .default 1.0,
      }

      ; Minimum size is 1pt x 1pt. Conversion follows from
      ; https://www.w3.org/TR/css3-values/#absolute-lengths
      browsingContext.PrintPageParameters = {
        ? height: (float .ge 0.0352) .default 27.94,
        ? width: (float .ge 0.0352) .default 21.59,
      }
```

```cddl
browsingContext.PrintResult = {
          data: text
        }
```

```cddl
browsingContext.Reload = (
        method: "browsingContext.reload",
        params: browsingContext.ReloadParameters
      )

      browsingContext.ReloadParameters = {
        context: browsingContext.BrowsingContext,
        ? ignoreCache: bool,
        ? wait: browsingContext.ReadinessState,
      }
```

```cddl
browsingContext.ReloadResult = browsingContext.NavigateResult
```

```cddl
browsingContext.SetBypassCSP = (
        method: "browsingContext.setBypassCSP",
        params: browsingContext.SetBypassCSPParameters
      )

      browsingContext.SetBypassCSPParameters = {
        bypass: true / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
browsingContext.SetBypassCSPResult = EmptyResult
```

```cddl
browsingContext.SetViewport = (
        method: "browsingContext.setViewport",
        params: browsingContext.SetViewportParameters
      )

      browsingContext.SetViewportParameters = {
        ? context: browsingContext.BrowsingContext,
        ? viewport: browsingContext.Viewport / null,
        ? devicePixelRatio: (float .gt 0.0) / null,
        ? userContexts: [+browser.UserContext],
      }

      browsingContext.Viewport = {
        width: js-uint,
        height: js-uint,
      }
```

```cddl
browsingContext.SetViewportResult = EmptyResult
```

```cddl
browsingContext.StartScreencast = (
        method: "browsingContext.startScreencast",
        params: browsingContext.StartScreencastParameters
      )

      browsingContext.StartScreencastParameters = {
        context: browsingContext.BrowsingContext,
        ? mimeType: text,
        ? video: browsingContext.MediaTrackConstraints,
        ? audio: bool .default false,
      }

      browsingContext.MediaTrackConstraints = {
         ? width: js-uint,
         ? height: js-uint,
         ? frameRate: js-uint,
      }
```

```cddl
browsingContext.StartScreencastResult = {
         screencast: browsingContext.Screencast,
         path: text
      }
```

```cddl
browsingContext.Screencast = text
```

```cddl
browsingContext.StopScreencast = (
        method: "browsingContext.stopScreencast",
        params: browsingContext.StopScreencastParameters
      )

      browsingContext.StopScreencastParameters = {
        screencast: browsingContext.Screencast
      }
```

```cddl
browsingContext.StopScreencastResult = {
         path: text,
         ? error: text
      }
```

```cddl
browsingContext.TraverseHistory = (
        method: "browsingContext.traverseHistory",
        params: browsingContext.TraverseHistoryParameters
      )

      browsingContext.TraverseHistoryParameters = {
        context: browsingContext.BrowsingContext,
        delta: js-int,
      }
```

```cddl
browsingContext.TraverseHistoryResult = EmptyResult
```

```cddl
browsingContext.ContextCreated = (
         method: "browsingContext.contextCreated",
         params: browsingContext.Info
        )
```

```cddl
browsingContext.ContextDestroyed = (
         method: "browsingContext.contextDestroyed",
         params: browsingContext.Info
        )
```

```cddl
browsingContext.NavigationStarted = (
         method: "browsingContext.navigationStarted",
         params: browsingContext.NavigationInfo
        )
```

```cddl
browsingContext.FragmentNavigated = (
         method: "browsingContext.fragmentNavigated",
         params: browsingContext.NavigationInfo
        )
```

```cddl
browsingContext.HistoryUpdated = (
          method: "browsingContext.historyUpdated",
          params: browsingContext.HistoryUpdatedParameters
        )

        browsingContext.HistoryUpdatedParameters = {
          context: browsingContext.BrowsingContext,
          timestamp: js-uint,
          url: text,
          ? userContext: browser.UserContext
        }
```

```cddl
browsingContext.DomContentLoaded = (
         method: "browsingContext.domContentLoaded",
         params: browsingContext.NavigationInfo
        )
```

```cddl
browsingContext.Load = (
         method: "browsingContext.load",
         params: browsingContext.NavigationInfo
        )
```

```cddl
browsingContext.DownloadWillBegin = (
         method: "browsingContext.downloadWillBegin",
         params: browsingContext.DownloadWillBeginParams
        )

        browsingContext.DownloadWillBeginParams = {
          download: browsingContext.Download,
          suggestedFilename: text,
          browsingContext.BaseNavigationInfo
        }
```

```cddl
browsingContext.DownloadEnd = (
          method: "browsingContext.downloadEnd",
          params: browsingContext.DownloadEndParams
        )

        browsingContext.DownloadEndParams = {
          (
            browsingContext.DownloadCanceledParams //
            browsingContext.DownloadCompleteParams
          )
        }

        browsingContext.DownloadCanceledParams = (
          status: "canceled",
          download: browsingContext.Download,
          browsingContext.BaseNavigationInfo
        )

        browsingContext.DownloadCompleteParams = (
          status: "complete",
          download: browsingContext.Download,
          filepath: text / null,
          browsingContext.BaseNavigationInfo
        )
```

```cddl
browsingContext.NavigationAborted = (
         method: "browsingContext.navigationAborted",
         params: browsingContext.NavigationInfo
        )
```

```cddl
browsingContext.NavigationCommitted = (
         method: "browsingContext.navigationCommitted",
         params: browsingContext.NavigationInfo
        )
```

```cddl
browsingContext.NavigationFailed = (
         method: "browsingContext.navigationFailed",
         params: browsingContext.NavigationInfo
        )
```

```cddl
browsingContext.UserPromptClosed = (
          method: "browsingContext.userPromptClosed",
          params: browsingContext.UserPromptClosedParameters
        )

        browsingContext.UserPromptClosedParameters = {
          context: browsingContext.BrowsingContext,
          accepted: bool,
          type: browsingContext.UserPromptType,
          ? userContext: browser.UserContext,
          ? userText: text
        }
```

```cddl
browsingContext.UserPromptOpened = (
          method: "browsingContext.userPromptOpened",
          params: browsingContext.UserPromptOpenedParameters
        )

        browsingContext.UserPromptOpenedParameters = {
          context: browsingContext.BrowsingContext,
          handler: session.UserPromptHandlerType,
          message: text,
          type: browsingContext.UserPromptType,
          ? userContext: browser.UserContext,
          ? defaultValue: text
        }
```

## Module: emulation

```cddl
EmulationCommand = (
  emulation.SetForcedColorsModeThemeOverride //
  emulation.SetGeolocationOverride //
  emulation.SetLocaleOverride //
  emulation.SetMediaFeaturesOverride //
  emulation.SetNetworkConditions //
  emulation.SetScreenOrientationOverride //
  emulation.SetScreenSettingsOverride //
  emulation.SetScriptingEnabled //
  emulation.SetScrollbarTypeOverride //
  emulation.SetTimezoneOverride //
  emulation.SetTouchOverride //
  emulation.SetUserAgentOverride //
  emulation.SetViewportMetaOverride
)
```

```cddl
EmulationResult = (
  emulation.SetForcedColorsModeThemeOverrideResult /
  emulation.SetGeolocationOverrideResult /
  emulation.SetLocaleOverrideResult /
  emulation.SetMediaFeaturesOverrideResult /
  emulation.SetScreenOrientationOverrideResult /
  emulation.SetScriptingEnabledResult /
  emulation.SetScrollbarTypeOverrideResult /
  emulation.SetTimezoneOverrideResult /
  emulation.SetTouchOverrideResult /
  emulation.SetUserAgentOverrideResult /
  emulation.SetViewportMetaOverrideResult
)
```

```cddl
emulation.SetForcedColorsModeThemeOverride = (
        method: "emulation.setForcedColorsModeThemeOverride",
        params: emulation.SetForcedColorsModeThemeOverrideParameters
      )

      emulation.SetForcedColorsModeThemeOverrideParameters = {
        theme: emulation.ForcedColorsModeTheme / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }

      emulation.ForcedColorsModeTheme = "light" / "dark"
```

```cddl
emulation.SetForcedColorsModeThemeOverrideResult = EmptyResult
```

```cddl
emulation.SetGeolocationOverride = (
        method: "emulation.setGeolocationOverride",
        params: emulation.SetGeolocationOverrideParameters
      )

      emulation.SetGeolocationOverrideParameters = {
        (
          (coordinates: emulation.GeolocationCoordinates / null) //
          (error: emulation.GeolocationPositionError)
        ),
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }

      emulation.GeolocationCoordinates = {
         latitude: -90.0..90.0,
         longitude: -180.0..180.0,
         ? accuracy: (float .ge 0.0) .default 1.0,
         ? altitude: float / null .default null,
         ? altitudeAccuracy: (float .ge 0.0) / null .default null,
         ? heading: (0.0...360.0) / null .default null,
         ? speed: (float .ge 0.0) / null .default null,
      }

      emulation.GeolocationPositionError = {
         type: "positionUnavailable"
      }
```

```cddl
emulation.SetGeolocationOverrideResult = EmptyResult
```

```cddl
emulation.SetLocaleOverride = (
        method: "emulation.setLocaleOverride",
        params: emulation.SetLocaleOverrideParameters
      )

      emulation.SetLocaleOverrideParameters = {
        locale: text / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetLocaleOverrideResult = EmptyResult
```

```cddl
emulation.SetMediaFeaturesOverride = (
        method: "emulation.setMediaFeaturesOverride",
        params: emulation.SetMediaFeaturesOverrideParameters
      )

      emulation.SetMediaFeaturesOverrideParameters = {
        features: emulation.MediaFeatures / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }

      emulation.MediaFeatures = [emulation.MediaFeature]

      emulation.MediaFeature = {
         name: text
         value: text
      }
```

```cddl
emulation.SetMediaFeaturesOverrideResult = EmptyResult
```

```cddl
emulation.SetNetworkConditions = (
        method: "emulation.setNetworkConditions",
        params: emulation.SetNetworkConditionsParameters
      )

      emulation.SetNetworkConditionsParameters = {
        networkConditions: emulation.NetworkConditions / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }

      emulation.NetworkConditions = emulation.NetworkConditionsOffline

      emulation.NetworkConditionsOffline = {
        type: "offline"
      }
```

```cddl
emulation.SetNetworkConditionsResult = EmptyResult
```

```cddl
emulation.SetScreenSettingsOverride = (
        method: "emulation.setScreenSettingsOverride",
        params: emulation.SetScreenSettingsOverrideParameters
      )

      emulation.ScreenArea = {
        width: js-uint,
        height: js-uint
      }

      emulation.SetScreenSettingsOverrideParameters = {
        screenArea: emulation.ScreenArea / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetScreenSettingsOverrideResult = EmptyResult
```

```cddl
emulation.SetScreenOrientationOverride = (
        method: "emulation.setScreenOrientationOverride",
        params: emulation.SetScreenOrientationOverrideParameters
      )

      emulation.ScreenOrientationNatural = "portrait" / "landscape"
      emulation.ScreenOrientationType = "portrait-primary" / "portrait-secondary" / "landscape-primary" / "landscape-secondary"

      emulation.ScreenOrientation = {
        natural: emulation.ScreenOrientationNatural,
        type: emulation.ScreenOrientationType
      }

      emulation.SetScreenOrientationOverrideParameters = {
        screenOrientation: emulation.ScreenOrientation / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetScreenOrientationOverrideResult = EmptyResult
```

```cddl
emulation.SetUserAgentOverride = (
        method: "emulation.setUserAgentOverride",
        params: emulation.SetUserAgentOverrideParameters
      )

      emulation.SetUserAgentOverrideParameters = {
        userAgent: text / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetUserAgentOverrideResult = EmptyResult
```

```cddl
emulation.SetViewportMetaOverride = (
        method: "emulation.setViewportMetaOverride",
        params: emulation.SetViewportMetaOverrideParameters
      )

      emulation.SetViewportMetaOverrideParameters = {
        viewportMeta: true / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetViewportMetaOverrideResult = EmptyResult
```

```cddl
emulation.SetScriptingEnabled = (
        method: "emulation.setScriptingEnabled",
        params: emulation.SetScriptingEnabledParameters
      )

      emulation.SetScriptingEnabledParameters = {
        enabled: false / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetScriptingEnabledResult = EmptyResult
```

```cddl
emulation.SetScrollbarTypeOverride = (
        method: "emulation.setScrollbarTypeOverride",
        params: emulation.SetScrollbarTypeOverrideParameters
      )

      emulation.SetScrollbarTypeOverrideParameters = {
        scrollbarType: "classic" / "overlay" / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetScrollbarTypeOverrideResult = EmptyResult
```

```cddl
emulation.SetTimezoneOverride = (
        method: "emulation.setTimezoneOverride",
        params: emulation.SetTimezoneOverrideParameters
      )

      emulation.SetTimezoneOverrideParameters = {
        timezone: text / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetTimezoneOverrideResult = EmptyResult
```

```cddl
emulation.SetTouchOverride = (
        method: "emulation.setTouchOverride",
        params: emulation.SetTouchOverrideParameters
      )

      emulation.SetTouchOverrideParameters = {
        maxTouchPoints: (js-uint .ge 1) / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetTouchOverrideResult = EmptyResult
```

## Module: network

```cddl
NetworkCommand = (
  network.AddDataCollector //
  network.AddIntercept //
  network.ContinueRequest //
  network.ContinueResponse //
  network.ContinueWithAuth //
  network.DisownData //
  network.FailRequest //
  network.GetData //
  network.ProvideResponse //
  network.RemoveDataCollector //
  network.RemoveIntercept //
  network.SetCacheBehavior //
  network.SetExtraHeaders
)
```

```cddl
NetworkResult = (
  network.AddDataCollectorResult /
  network.AddInterceptResult /
  network.ContinueRequestResult /
  network.ContinueResponseResult /
  network.ContinueWithAuthResult /
  network.DisownDataResult /
  network.FailRequestResult /
  network.GetDataResult /
  network.ProvideResponseResult /
  network.RemoveDataCollectorResult /
  network.RemoveInterceptResult /
  network.SetCacheBehaviorResult /
  network.SetExtraHeadersResult
)

NetworkEvent = (
    network.AuthRequired //
    network.BeforeRequestSent //
    network.FetchError //
    network.ResponseCompleted //
    network.ResponseStarted
)
```

```cddl
network.AuthChallenge = {
  scheme: text,
  realm: text,
}
```

```cddl
network.AuthCredentials = {
  type: "password",
  username: text,
  password: text,
}
```

```cddl
network.BaseParameters = (
    context: browsingContext.BrowsingContext / null,
    isBlocked: bool,
    navigation: browsingContext.Navigation / null,
    redirectCount: js-uint,
    request: network.RequestData,
    timestamp: js-uint,
    ? userContext: browser.UserContext / null,
    ? intercepts: [+network.Intercept]
)
```

```cddl
network.BytesValue = network.StringValue / network.Base64Value;

network.StringValue = {
  type: "string",
  value: text,
}

network.Base64Value = {
  type: "base64",
  value: text,
}
```

```cddl
network.Collector = text
```

```cddl
network.CollectorType = "blob"
```

```cddl
network.SameSite = "strict" / "lax" / "none" / "default"

<!--
Modifications to this definition should be reflected in
`network.SetCookieHeader`, `storage.CookieFilter`, and `storage.PartialCookie`.
-->
network.Cookie = {
    name: text,
    value: network.BytesValue,
    domain: text,
    path: text,
    size: js-uint,
    httpOnly: bool,
    secure: bool,
    sameSite: network.SameSite,
    ? expiry: js-uint,
    Extensible,
}
```

```cddl
network.CookieHeader = {
    name: text,
    value: network.BytesValue,
}
```

```cddl
network.DataType = "request" / "response"
```

```cddl
network.FetchTimingInfo = {
    timeOrigin: float,
    requestTime: float,
    redirectStart: float,
    redirectEnd: float,
    fetchStart: float,
    dnsStart: float,
    dnsEnd: float,
    connectStart: float,
    connectEnd: float,
    tlsStart: float,
    <!-- tlsEnd: float this should be the same as connectEnd -->
    requestStart: float,
    responseStart: float,
    <!-- TODO responseHeadersEnd: float: Not sure quite what to use for this -->
    responseEnd: float,
}
```

```cddl
network.Header = {
  name: text,
  value: network.BytesValue,
}
```

```cddl
network.Initiator = {
    ? columnNumber: js-uint,
    ? lineNumber: js-uint,
    ? request: network.Request,
    ? stackTrace: script.StackTrace,
    ? type: "parser" / "script" / "preflight" / "other"
}
```

```cddl
network.Intercept = text
```

```cddl
network.Request = text;
```

```cddl
network.RequestData = {
    request: network.Request,
    url: text,
    method: text,
    headers: [*network.Header],
    cookies: [*network.Cookie],
    headersSize: js-uint,
    bodySize: js-uint / null,
    destination: text,
    initiatorType: text / null,
    timings: network.FetchTimingInfo,
}
```

```cddl
network.ResponseContent = {
    size: js-uint
}
```

```cddl
network.ResponseData = {
    url: text,
    protocol: text,
    status: js-uint,
    statusText: text,
    fromCache: bool,
    headers: [*network.Header],
    mimeType: text,
    bytesReceived: js-uint,
    headersSize: js-uint / null,
    bodySize: js-uint / null,
    content: network.ResponseContent,
    ?authChallenges: [*network.AuthChallenge],
}
```

```cddl
<!--
Modifications to this definition should be reflected in
`network.Cookie`, `storage.CookieFilter`, and `storage.PartialCookie`.
-->
network.SetCookieHeader = {
    name: text,
    value: network.BytesValue,
    ? domain: text,
    ? httpOnly: bool,
    ? expiry: text,
    ? maxAge: js-int,
    ? path: text,
    ? sameSite: network.SameSite,
    ? secure: bool,
}
```

```cddl
network.UrlPattern = (
  network.UrlPatternPattern /
  network.UrlPatternString
)

network.UrlPatternPattern = {
    type: "pattern",
    ?protocol: text,
    ?hostname: text,
    ?port: text,
    ?pathname: text,
    ?search: text,
}


network.UrlPatternString = {
    type: "string",
    pattern: text,
}
```

```cddl
network.AddDataCollector = (
        method: "network.addDataCollector",
        params: network.AddDataCollectorParameters
      )

      network.AddDataCollectorParameters = {
        dataTypes: [+network.DataType],
        maxEncodedDataSize: js-uint,
        ? collectorType: network.CollectorType .default "blob",
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
network.AddDataCollectorResult = {
        collector: network.Collector
      }
```

```cddl
network.AddIntercept = (
        method: "network.addIntercept",
        params: network.AddInterceptParameters
      )

      network.AddInterceptParameters = {
        phases: [+network.InterceptPhase],
        ? contexts: [+browsingContext.BrowsingContext],
        ? urlPatterns: [*network.UrlPattern],
      }

      network.InterceptPhase = "beforeRequestSent" / "responseStarted" /
                               "authRequired"
```

```cddl
network.AddInterceptResult = {
        intercept: network.Intercept
      }
```

```cddl
network.ContinueRequest = (
        method: "network.continueRequest",
        params: network.ContinueRequestParameters
      )

      network.ContinueRequestParameters = {
        request: network.Request,
        ?body: network.BytesValue,
        ?cookies: [*network.CookieHeader],
        ?headers: [*network.Header],
        ?method: text,
        ?url: text,
      }
```

```cddl
network.ContinueRequestResult = EmptyResult
```

```cddl
network.ContinueResponse = (
        method: "network.continueResponse",
        params: network.ContinueResponseParameters
      )

      network.ContinueResponseParameters = {
        request: network.Request,
        ?cookies: [*network.SetCookieHeader]
        ?credentials: network.AuthCredentials,
        ?headers: [*network.Header],
        ?reasonPhrase: text,
        ?statusCode: js-uint,
      }
```

```cddl
network.ContinueResponseResult = EmptyResult
```

```cddl
network.ContinueWithAuth = (
        method: "network.continueWithAuth",
        params: network.ContinueWithAuthParameters
      )

      network.ContinueWithAuthParameters = {
        request: network.Request,
        (network.ContinueWithAuthCredentials // network.ContinueWithAuthNoCredentials)
      }

      network.ContinueWithAuthCredentials = (
        action: "provideCredentials", <!-- or "provide credentials" or
      "providecredentials" or something else -->
        credentials: network.AuthCredentials
      )

      network.ContinueWithAuthNoCredentials = (
        action: "default" / "cancel"
      )
```

```cddl
network.ContinueWithAuthResult = EmptyResult
```

```cddl
network.DisownData = (
        method: "network.disownData",
        params: network.DisownDataParameters
      )

      network.DisownDataParameters = {
        dataType: network.DataType,
        collector: network.Collector,
        request: network.Request,
      }
```

```cddl
network.DisownDataResult = EmptyResult
```

```cddl
network.FailRequest = (
        method: "network.failRequest",
        params: network.FailRequestParameters
      )

      network.FailRequestParameters = {
        request: network.Request,
      }
```

```cddl
network.FailRequestResult = EmptyResult
```

```cddl
network.GetData = (
        method: "network.getData",
        params: network.GetDataParameters
      )

      network.GetDataParameters = {
        dataType: network.DataType,
        ? collector: network.Collector,
        ? disown: bool .default false,
        request: network.Request,
      }
```

```cddl
network.GetDataResult = {
        bytes: network.BytesValue,
      }
```

```cddl
network.ProvideResponse = (
        method: "network.provideResponse",
        params: network.ProvideResponseParameters
      )

      network.ProvideResponseParameters = {
        request: network.Request,
        ?body: network.BytesValue,
        ?cookies: [*network.SetCookieHeader],
        ?headers: [*network.Header],
        ?reasonPhrase: text,
        ?statusCode: js-uint,
      }
```

```cddl
network.ProvideResponseResult = EmptyResult
```

```cddl
network.RemoveDataCollector = (
        method: "network.removeDataCollector",
        params: network.RemoveDataCollectorParameters
      )

      network.RemoveDataCollectorParameters = {
        collector: network.Collector
      }
```

```cddl
network.RemoveDataCollectorResult = EmptyResult
```

```cddl
network.RemoveIntercept = (
        method: "network.removeIntercept",
        params: network.RemoveInterceptParameters
      )

      network.RemoveInterceptParameters = {
        intercept: network.Intercept
      }
```

```cddl
network.RemoveInterceptResult = EmptyResult
```

```cddl
network.SetCacheBehavior = (
        method: "network.setCacheBehavior",
        params: network.SetCacheBehaviorParameters
      )

      network.SetCacheBehaviorParameters = {
        cacheBehavior: "default" / "bypass",
        ? contexts: [+browsingContext.BrowsingContext]
      }
```

```cddl
network.SetCacheBehaviorResult = EmptyResult
```

```cddl
network.SetExtraHeaders = (
        method: "network.setExtraHeaders",
        params: network.SetExtraHeadersParameters
      )

      network.SetExtraHeadersParameters = {
        headers: [*network.Header]
        ? contexts: [+browsingContext.BrowsingContext]
        ? userContexts: [+browser.UserContext]
      }
```

```cddl
network.SetExtraHeadersResult = EmptyResult
```

```cddl
network.AuthRequired = (
        method: "network.authRequired",
        params: network.AuthRequiredParameters
      )

      network.AuthRequiredParameters = {
        network.BaseParameters,
        response: network.ResponseData
      }
```

```cddl
network.BeforeRequestSent = (
         method: "network.beforeRequestSent",
         params: network.BeforeRequestSentParameters
        )

       network.BeforeRequestSentParameters = {
         network.BaseParameters,
         ? initiator: network.Initiator,
       }
```

```cddl
network.FetchError = (
         method: "network.fetchError",
         params: network.FetchErrorParameters
        )

       network.FetchErrorParameters = {
         network.BaseParameters,
         errorText: text,
       }
```

```cddl
network.ResponseCompleted = (
         method: "network.responseCompleted",
         params: network.ResponseCompletedParameters
        )

       network.ResponseCompletedParameters = {
         network.BaseParameters,
         response: network.ResponseData,
       }
```

```cddl
network.ResponseStarted = (
         method: "network.responseStarted",
         params: network.ResponseStartedParameters
        )

       network.ResponseStartedParameters = {
         network.BaseParameters,
         response: network.ResponseData,
       }
```

## Module: script

```cddl
ScriptCommand = (
  script.AddPreloadScript //
  script.CallFunction //
  script.Disown //
  script.Evaluate //
  script.GetRealms //
  script.RemovePreloadScript
)
```

```cddl
ScriptResult = (
  script.AddPreloadScriptResult /
  script.CallFunctionResult /
  script.DisownResult /
  script.EvaluateResult /
  script.GetRealmsResult /
  script.RemovePreloadScriptResult
)

ScriptEvent = (
  script.Message //
  script.RealmCreated //
  script.RealmDestroyed
)
```

```cddl
script.Channel = text;
```

```cddl
script.ChannelValue = {
  type: "channel",
  value: script.ChannelProperties,
}

script.ChannelProperties = {
  channel: script.Channel,
  ? serializationOptions: script.SerializationOptions,
  ? ownership: script.ResultOwnership,
}
```

```cddl
script.EvaluateResult = (
  script.EvaluateResultSuccess /
  script.EvaluateResultException
)

script.EvaluateResultSuccess = {
  type: "success",
  result: script.RemoteValue,
  realm: script.Realm
}

script.EvaluateResultException = {
  type: "exception",
  exceptionDetails: script.ExceptionDetails
  realm: script.Realm
}
```

```cddl
script.ExceptionDetails = {
  columnNumber: js-uint,
  exception: script.RemoteValue,
  lineNumber: js-uint,
  stackTrace: script.StackTrace,
  text: text,
}
```

```cddl
script.Handle = text;
```

```cddl
script.InternalId = text;
```

```cddl
script.LocalValue = (
  script.RemoteReference /
  script.PrimitiveProtocolValue /
  script.ChannelValue /
  script.ArrayLocalValue /
  { script.DateLocalValue } /
  script.MapLocalValue /
  script.ObjectLocalValue /
  { script.RegExpLocalValue } /
  script.SetLocalValue
)

script.ListLocalValue = [*script.LocalValue];

script.ArrayLocalValue = {
  type: "array",
  value: script.ListLocalValue,
}

script.DateLocalValue = (
  type: "date",
  value: text
)

script.MappingLocalValue = [*[(script.LocalValue / text), script.LocalValue]];

script.MapLocalValue = {
  type: "map",
  value: script.MappingLocalValue,
}

script.ObjectLocalValue = {
  type: "object",
  value: script.MappingLocalValue,
}

script.RegExpValue = {
  pattern: text,
  ? flags: text,
}

script.RegExpLocalValue = (
  type: "regexp",
  value: script.RegExpValue,
)

script.SetLocalValue = {
  type: "set",
  value: script.ListLocalValue,
}
```

```cddl
script.PreloadScript = text;
```

```cddl
script.Realm = text;
```

```cddl
script.PrimitiveProtocolValue = (
  script.UndefinedValue /
  script.NullValue /
  script.StringValue /
  script.NumberValue /
  script.BooleanValue /
  script.BigIntValue
)

script.UndefinedValue = {
  type: "undefined",
}

script.NullValue = {
  type: "null",
}

script.StringValue = {
  type: "string",
  value: text,
}

script.SpecialNumber = "NaN" / "-0" / "Infinity" / "-Infinity";

script.NumberValue = {
  type: "number",
  value: number / script.SpecialNumber,
}

script.BooleanValue = {
  type: "boolean",
  value: bool,
}

script.BigIntValue = {
  type: "bigint",
  value: text,
}
```

```cddl
script.RealmInfo = (
  script.WindowRealmInfo /
  script.DedicatedWorkerRealmInfo /
  script.SharedWorkerRealmInfo /
  script.ServiceWorkerRealmInfo /
  script.WorkerRealmInfo /
  script.PaintWorkletRealmInfo /
  script.AudioWorkletRealmInfo /
  script.WorkletRealmInfo
)

script.BaseRealmInfo = (
  realm: script.Realm,
  origin: text
)

script.WindowRealmInfo = {
  script.BaseRealmInfo,
  type: "window",
  context: browsingContext.BrowsingContext,
  ? userContext: browser.UserContext,
  ? sandbox: text
}

script.DedicatedWorkerRealmInfo = {
  script.BaseRealmInfo,
  type: "dedicated-worker",
  owners: [script.Realm]
}

script.SharedWorkerRealmInfo = {
  script.BaseRealmInfo,
  type: "shared-worker"
}

script.ServiceWorkerRealmInfo = {
  script.BaseRealmInfo,
  type: "service-worker"
}

script.WorkerRealmInfo = {
  script.BaseRealmInfo,
  type: "worker"
}

script.PaintWorkletRealmInfo = {
  script.BaseRealmInfo,
  type: "paint-worklet"
}

script.AudioWorkletRealmInfo = {
  script.BaseRealmInfo,
  type: "audio-worklet"
}

script.WorkletRealmInfo = {
  script.BaseRealmInfo,
  type: "worklet"
}
```

```cddl
script.RealmType = "window" / "dedicated-worker" / "shared-worker" / "service-worker" /
                   "worker" / "paint-worklet" / "audio-worklet" / "worklet"
```

```cddl
<!-- This is specifically ordered in the order in which matches need to be -->
<!-- evaluated, since the definitions are overlapping -->
script.RemoteReference = (
  script.SharedReference /
  script.RemoteObjectReference
)

script.SharedReference = {
   sharedId: script.SharedId
   <!-- Ensure that if we have a handle, it at least has the correct type -->
   ? handle: script.Handle,
   Extensible
}

script.RemoteObjectReference = {
   handle: script.Handle,
   <!-- This shouldn't ever match. The problem is that Extensible would
   otherwise allow this to match a non-text sharedId -->
   ? sharedId: script.SharedId
   Extensible
}
```

```cddl
script.RemoteValue = (
  script.PrimitiveProtocolValue /
  script.SymbolRemoteValue /
  script.ArrayRemoteValue /
  script.ObjectRemoteValue /
  script.FunctionRemoteValue /
  script.RegExpRemoteValue /
  script.DateRemoteValue /
  script.MapRemoteValue /
  script.SetRemoteValue /
  script.WeakMapRemoteValue /
  script.WeakSetRemoteValue /
  script.GeneratorRemoteValue /
  script.ErrorRemoteValue /
  script.ProxyRemoteValue /
  script.PromiseRemoteValue /
  script.TypedArrayRemoteValue /
  script.ArrayBufferRemoteValue /
  script.NodeListRemoteValue /
  script.HTMLCollectionRemoteValue /
  script.NodeRemoteValue /
  script.WindowProxyRemoteValue
)

script.ListRemoteValue = [*script.RemoteValue];

script.MappingRemoteValue = [*[(script.RemoteValue / text), script.RemoteValue]];

script.SymbolRemoteValue = {
  type: "symbol",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.ArrayRemoteValue = {
  type: "array",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.ListRemoteValue,
}

script.ObjectRemoteValue = {
  type: "object",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.MappingRemoteValue,
}

script.FunctionRemoteValue = {
  type: "function",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.RegExpRemoteValue = {
  script.RegExpLocalValue,
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.DateRemoteValue = {
  script.DateLocalValue,
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.MapRemoteValue = {
  type: "map",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.MappingRemoteValue,
}

script.SetRemoteValue = {
  type: "set",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.ListRemoteValue
}

script.WeakMapRemoteValue = {
  type: "weakmap",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.WeakSetRemoteValue = {
  type: "weakset",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.GeneratorRemoteValue = {
  type: "generator",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.ErrorRemoteValue = {
  type: "error",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.ProxyRemoteValue = {
  type: "proxy",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.PromiseRemoteValue = {
  type: "promise",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.TypedArrayRemoteValue = {
  type: "typedarray",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.ArrayBufferRemoteValue = {
  type: "arraybuffer",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.NodeListRemoteValue = {
  type: "nodelist",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.ListRemoteValue,
}

script.HTMLCollectionRemoteValue = {
  type: "htmlcollection",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.ListRemoteValue,
}

script.NodeRemoteValue = {
  type: "node",
  ? sharedId: script.SharedId,
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.NodeProperties,
}

script.NodeProperties = {
  nodeType: js-uint,
  childNodeCount: js-uint,
  ? attributes: {*text => text},
  ? children: [*script.NodeRemoteValue],
  ? localName: text,
  ? mode: "open" / "closed",
  ? namespaceURI: text,
  ? nodeValue: text,
  ? shadowRoot: script.NodeRemoteValue / null,
}

script.WindowProxyRemoteValue = {
  type: "window",
  value: script.WindowProxyProperties,
  ? handle: script.Handle,
  ? internalId: script.InternalId
}

script.WindowProxyProperties = {
  context: browsingContext.BrowsingContext
}
```

```cddl
script.ResultOwnership = "root" / "none"
```

```cddl
script.SerializationOptions = {
  ? maxDomDepth: (js-uint / null) .default 0,
  ? maxObjectDepth: (js-uint / null) .default null,
  ? includeShadowTree: ("none" / "open" / "all") .default "none",
}
```

```cddl
script.SharedId = text;
```

```cddl
script.StackFrame = {
  columnNumber: js-uint,
  functionName: text,
  lineNumber: js-uint,
  url: text,
}
```

```cddl
script.StackTrace = {
  callFrames: [*script.StackFrame],
}
```

```cddl
script.Source = {
  realm: script.Realm,
  ? context: browsingContext.BrowsingContext,
  ? userContext: browser.UserContext
}
```

```cddl
script.RealmTarget = {
  realm: script.Realm
}

script.ContextTarget = {
  context: browsingContext.BrowsingContext,
  ? sandbox: text
}

script.Target = (
  script.ContextTarget /
  script.RealmTarget
)
```

```cddl
script.AddPreloadScript = (
        method: "script.addPreloadScript",
        params: script.AddPreloadScriptParameters
      )

      script.AddPreloadScriptParameters = {
        functionDeclaration: text,
        ? arguments: [*script.ChannelValue],
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
        ? sandbox: text
      }
```

```cddl
script.AddPreloadScriptResult = {
        script: script.PreloadScript
      }
```

```cddl
script.Disown = (
        method: "script.disown",
        params: script.DisownParameters
      )

      script.DisownParameters = {
        handles: [*script.Handle]
        target: script.Target;
      }
```

```cddl
script.DisownResult = EmptyResult
```

```cddl
script.CallFunction = (
        method: "script.callFunction",
        params: script.CallFunctionParameters
      )

      script.CallFunctionParameters = {
        functionDeclaration: text,
        awaitPromise: bool,
        target: script.Target,
        ? arguments: [*script.LocalValue],
        ? resultOwnership: script.ResultOwnership,
        ? serializationOptions: script.SerializationOptions,
        ? this: script.LocalValue,
        ? userActivation: bool .default false,
      }
```

```cddl
script.CallFunctionResult = script.EvaluateResult
```

```cddl
script.Evaluate = (
        method: "script.evaluate",
        params: script.EvaluateParameters
      )

      script.EvaluateParameters = {
        expression: text,
        target: script.Target,
        awaitPromise: bool,
        ? resultOwnership: script.ResultOwnership,
        ? serializationOptions: script.SerializationOptions,
        ? userActivation: bool .default false,
      }
```

```cddl
script.GetRealms = (
        method: "script.getRealms",
        params: script.GetRealmsParameters
      )

      script.GetRealmsParameters = {
        ? context: browsingContext.BrowsingContext,
        ? type: script.RealmType,
      }
```

```cddl
script.GetRealmsResult = {
        realms: [*script.RealmInfo]
      }
```

```cddl
script.RemovePreloadScript = (
        method: "script.removePreloadScript",
        params: script.RemovePreloadScriptParameters
      )

      script.RemovePreloadScriptParameters = {
        script: script.PreloadScript
      }
```

```cddl
script.RemovePreloadScriptResult = EmptyResult
```

```cddl
script.Message = (
         method: "script.message",
         params: script.MessageParameters
        )

       script.MessageParameters = {
         channel: script.Channel,
         data: script.RemoteValue,
         source: script.Source,
       }
```

```cddl
script.RealmCreated = (
         method: "script.realmCreated",
         params: script.RealmInfo
        )
```

```cddl
script.RealmDestroyed = (
         method: "script.realmDestroyed",
         params: script.RealmDestroyedParameters
       )

       script.RealmDestroyedParameters = {
         realm: script.Realm
       }
```

## Module: storage

```cddl
StorageCommand = (
  storage.DeleteCookies //
  storage.GetCookies //
  storage.SetCookie
)
```

```cddl
StorageResult = (
  storage.DeleteCookiesResult /
  storage.GetCookiesResult /
  storage.SetCookieResult
)
```

```cddl
storage.PartitionKey = {
  ? userContext: text,
  ? sourceOrigin: text,
  Extensible,
}
```

```cddl
storage.GetCookies = (
          method: "storage.getCookies",
          params: storage.GetCookiesParameters
        )

        <!--
        Modifications to this definition should be reflected in
        `network.Cookie`, `network.SetCookieHeader`, and `storage.PartialCookie`.
        -->
        storage.CookieFilter = {
          ? name: text,
          ? value: network.BytesValue,
          ? domain: text,
          ? path: text,
          ? size: js-uint,
          ? httpOnly: bool,
          ? secure: bool,
          ? sameSite: network.SameSite,
          ? expiry: js-uint,
          Extensible,
        }

        storage.BrowsingContextPartitionDescriptor = {
          type: "context",
          context: browsingContext.BrowsingContext
        }

        storage.StorageKeyPartitionDescriptor = {
          type: "storageKey",
          ? userContext: text,
          ? sourceOrigin: text,
          Extensible,
        }

        storage.PartitionDescriptor = (
          storage.BrowsingContextPartitionDescriptor /
          storage.StorageKeyPartitionDescriptor
        )

        storage.GetCookiesParameters = {
          ? filter: storage.CookieFilter,
          ? partition: storage.PartitionDescriptor,
        }
```

```cddl
storage.GetCookiesResult = {
        cookies: [*network.Cookie],
        partitionKey: storage.PartitionKey,
      }
```

```cddl
storage.SetCookie = (
          method: "storage.setCookie",
          params: storage.SetCookieParameters,
        )

        <!--
        Modifications to this definition should be reflected in
        `network.Cookie`, `network.SetCookieHeader`, and `storage.CookieFilter`.
        -->
        storage.PartialCookie = {
          name: text,
          value: network.BytesValue,
          domain: text,
          ? path: text,
          ? httpOnly: bool,
          ? secure: bool,
          ? sameSite: network.SameSite,
          ? expiry: js-uint,
          Extensible,
        }

        storage.SetCookieParameters = {
          cookie: storage.PartialCookie,
          ? partition: storage.PartitionDescriptor,
        }
```

```cddl
storage.SetCookieResult = {
        partitionKey: storage.PartitionKey
      }
```

```cddl
storage.DeleteCookies = (
          method: "storage.deleteCookies",
          params: storage.DeleteCookiesParameters,
        )

        storage.DeleteCookiesParameters = {
          ? filter: storage.CookieFilter,
          ? partition: storage.PartitionDescriptor,
        }
```

```cddl
storage.DeleteCookiesResult = {
          partitionKey: storage.PartitionKey
        }
```

## Module: log

```cddl
LogEvent = (
  log.EntryAdded
)
```

```cddl
log.Level = "debug" / "info" / "warn" / "error"

log.Entry = (
  log.GenericLogEntry /
  log.ConsoleLogEntry /
  log.JavascriptLogEntry
)

log.BaseLogEntry = (
  level: log.Level,
  source: script.Source,
  text: text / null,
  timestamp: js-uint,
  ? stackTrace: script.StackTrace,
)

log.GenericLogEntry = {
  log.BaseLogEntry,
  type: text,
}

log.ConsoleLogEntry = {
  log.BaseLogEntry,
  type: "console",
  method: text,
  args: [*script.RemoteValue],
}

log.JavascriptLogEntry = {
  log.BaseLogEntry,
  type: "javascript",
}
```

```cddl
log.EntryAdded = (
         method: "log.entryAdded",
         params: log.Entry,
        )
```

## Module: input

```cddl
InputCommand = (
  input.PerformActions //
  input.ReleaseActions //
  input.SetFiles
)
```

```cddl
InputResult = (
  input.PerformActionsResult /
  input.ReleaseActionsResult /
  input.SetFilesResult
)
```

```cddl
InputEvent = (
  input.FileDialogOpened
)
```

```cddl
input.ElementOrigin = {
  type: "element",
  element: script.SharedReference
}
```

```cddl
input.PerformActions = (
        method: "input.performActions",
        params: input.PerformActionsParameters
      )

      input.PerformActionsParameters = {
        context: browsingContext.BrowsingContext,
        actions: [*input.SourceActions]
      }

      input.SourceActions = (
        input.NoneSourceActions /
        input.KeySourceActions /
        input.PointerSourceActions /
        input.WheelSourceActions
      )

      input.NoneSourceActions = {
        type: "none",
        id: text,
        actions: [*input.NoneSourceAction]
      }

      input.NoneSourceAction = input.PauseAction

      input.KeySourceActions = {
        type: "key",
        id: text,
        actions: [*input.KeySourceAction]
      }

      input.KeySourceAction = (
        input.PauseAction /
        input.KeyDownAction /
        input.KeyUpAction
      )

      input.PointerSourceActions = {
        type: "pointer",
        id: text,
        ? parameters: input.PointerParameters,
        actions: [*input.PointerSourceAction]
      }

      input.PointerType = "mouse" / "pen" / "touch"

      input.PointerParameters = {
        ? pointerType: input.PointerType .default "mouse"
      }

      input.PointerSourceAction = (
        input.PauseAction /
        input.PointerDownAction /
        input.PointerUpAction /
        input.PointerMoveAction
      )

      input.WheelSourceActions = {
        type: "wheel",
        id: text,
        actions: [*input.WheelSourceAction]
      }

      input.WheelSourceAction = (
        input.PauseAction /
        input.WheelScrollAction
      )

      input.PauseAction = {
        type: "pause",
        ? duration: js-uint
      }

      input.KeyDownAction = {
        type: "keyDown",
        value: text
      }

      input.KeyUpAction = {
        type: "keyUp",
        value: text
      }

      input.PointerUpAction = {
        type: "pointerUp",
        button: js-uint,
      }

      input.PointerDownAction = {
        type: "pointerDown",
        button: js-uint,
        input.PointerCommonProperties
      }

      input.PointerMoveAction = {
        type: "pointerMove",
        x: float,
        y: float,
        ? duration: js-uint,
        ? origin: input.Origin,
        input.PointerCommonProperties
      }

      input.WheelScrollAction = {
        type: "scroll",
        x: js-int,
        y: js-int,
        deltaX: js-int,
        deltaY: js-int,
        ? duration: js-uint,
        ? origin: input.Origin .default "viewport",
      }

      input.PointerCommonProperties = (
        ? width: js-uint,
        ? height: js-uint,
        ? pressure: (0.0..1.0),
        ? tangentialPressure: (-1.0..1.0),
        ? twist: (0..359),
        ; 0 .. Math.PI / 2
        ? altitudeAngle: (0.0..1.5707963267948966),
        ; 0 .. 2 * Math.PI
        ? azimuthAngle: (0.0..6.283185307179586),
      )

      input.Origin = "viewport" / "pointer" / input.ElementOrigin
```

```cddl
input.PerformActionsResult = EmptyResult
```

```cddl
input.ReleaseActions = (
        method: "input.releaseActions",
        params: input.ReleaseActionsParameters
      )

      input.ReleaseActionsParameters = {
        context: browsingContext.BrowsingContext,
      }
```

```cddl
input.ReleaseActionsResult = EmptyResult
```

```cddl
input.SetFiles = (
        method: "input.setFiles",
        params: input.SetFilesParameters
      )

      input.SetFilesParameters = {
        context: browsingContext.BrowsingContext,
        element: script.SharedReference,
        files: [*text]
      }
```

```cddl
input.SetFilesResult = EmptyResult
```

```cddl
input.FileDialogOpened = (
            method: "input.fileDialogOpened",
            params: input.FileDialogInfo
         )

         input.FileDialogInfo = {
            context: browsingContext.BrowsingContext,
            ? userContext: browser.UserContext,
            ? element: script.SharedReference,
            multiple: bool,
         }
```

## Module: webExtension

```cddl
WebExtensionCommand = (
  webExtension.Install //
  webExtension.Uninstall
)
```

```cddl
WebExtensionResult = (
  webExtension.InstallResult /
  webExtension.UninstallResult
)
```

```cddl
webExtension.Extension = text
```

```cddl
webExtension.Install = (
         method: "webExtension.install",
         params: webExtension.InstallParameters
      )

      webExtension.InstallParameters = {
         extensionData: webExtension.ExtensionData,
      }

      webExtension.ExtensionData = (
         webExtension.ExtensionArchivePath /
         webExtension.ExtensionBase64Encoded /
         webExtension.ExtensionPath
      )

      webExtension.ExtensionPath = {
         type: "path",
         path: text,
      }

      webExtension.ExtensionArchivePath = {
         type: "archivePath",
         path: text,
      }

      webExtension.ExtensionBase64Encoded = {
         type: "base64",
         value: text,
      }
```

```cddl
webExtension.InstallResult = {
        extension: webExtension.Extension
      }
```

```cddl
webExtension.Uninstall = (
         method: "webExtension.uninstall",
         params: webExtension.UninstallParameters
      )

      webExtension.UninstallParameters = {
         extension: webExtension.Extension,
      }
```

```cddl
webExtension.UninstallResult = EmptyResult
```
